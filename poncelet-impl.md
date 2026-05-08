# Poncelet Visualizer — Implementation Plan

## Goal
Replace `_includes/conic-visualizer.html` with a Poncelet's Porism visualizer:
two ellipses (A outer, B inner), user clicks a starting point on A, the Poncelet
construction is drawn step by step with animation.

---

## Sub-tasks (implement in order)

### ✅ Step 1 — Validation helpers
File: `_includes/conic-visualizer.html` (script section)

Functions needed:
- `isEllipse(co)` → bool  
  Discriminant of quadratic part: `d²− 4ab < 0` AND quadratic form positive definite
  (`a > 0`, `b > 0`, `4ab − d² > 0`).
- `centerOf(co)` → `[cx, cy]`  
  Solve `∂F/∂x = 0, ∂F/∂y = 0`:  
  `2a·cx + d·cy + e = 0`  
  `d·cx + 2b·cy + f = 0`  
  Cramer: `det = 4ab − d²`, `cx = (−2b·e + d·f)/det`, `cy = (−2a·f + d·e)/det`.
- `isBInside(cA, cB)` → bool  
  Evaluate cA at the center of cB. If the sign equals the sign of cA at a known interior
  point (its own center), B is inside A.  
  Also require that the two conics have no real intersections (reuse existing `findPts`).

Display: a warning `<div>` below the inputs; hide it when inputs are valid.

---

### ✅ Step 2 — Snap click to outer conic A
Functions needed:
- `snapToA(mx, my, cA)` → `[x, y]`  
  Ray from center of A through (mx, my); parametrize as `(cx + t·(mx−cx), cy + t·(my−cy))`;
  substitute into A → quadratic in `t`; take the positive root (point on A in the direction
  of the click).

UI: add a click event listener on the canvas. On click, convert to math coords, call
`snapToA`, draw a highlighted dot, then trigger `startConstruction`.

---

### ✅ Step 3 — Tangent lines from point P to inner conic B
Functions needed:
- `polarLine(co, px, py)` → `{A, B, C}` (line `Ax + By + C = 0`)  
  Polar of P w.r.t. conic: `A = a·px + d/2·py + e/2`, `B = d/2·px + b·py + f/2`,
  `C = e/2·px + f/2·py + c`.
- `lineConicIntersect(line, co)` → `[[x1,y1],[x2,y2]]`  
  Parametrize line as `(x0 + t·dx, y0 + t·dy)` (pick a base point on the line),
  substitute into conic, solve quadratic in `t`.
- `tangentPointsOnB(P, cB)` → `[[q1x,q1y],[q2x,q2y]]`  
  = intersections of `polarLine(cB, P)` with cB. These are the two tangency points.

---

### ✅ Step 4 — One Poncelet step
Function: `ponceletStep(P, prevQ, cA, cB)` → `{nextP, tangentPt, tangentLine}`

1. `[Q1, Q2] = tangentPointsOnB(P, cB)`
2. Pick the tangent point Q that is NOT `prevQ` (distance > ε = 1e-3).  
   On the very first step `prevQ = null`, pick Q1 (or whichever gives a sensible direction).
3. Line through P and Q → `lineConicIntersect` with cA → two points;  
   take the one that is NOT P (distance from P > ε).
4. Return `{ nextP, tangentPt: Q, tangentLine: [P, nextP] }`.

---

### ✅ Step 5 — Full construction loop + closure detection
Function: `buildConstruction(startP, cA, cB, maxSteps=10)`  
Returns array of `{ point, tangentPt, line }` objects.

Loop:
```
P = startP, prevQ = null
for i in 0..maxSteps-1:
    step = ponceletStep(P, prevQ, cA, cB)
    push step to results
    prevQ = step.tangentPt
    P = step.nextP
    if dist(P, startP) < 1e-2: mark as closed n-gon, break
```

---

### ✅ Step 6 — Drawing
Functions:
- `drawEllipses(ctx, cA, cB)` — the two ellipses (reuse sign-change raster from current code)
- `drawStep(ctx, step, alpha)` — draw the tangent line and the new point; `alpha` for fade-in
- `drawStartPoint(ctx, P)` — orange dot with a slightly larger ring

---

### ✅ Step 7 — Animation
State machine:
```
state = { steps[], currentIdx, animating }
```
- "Draw" button: run validation, clear canvas, draw ellipses, wait for click.
- On click: snap to A, call `buildConstruction`, store steps, start animation.
- Animation: every 600 ms, draw next step (tangent line + new point).
- After all steps: display result message ("Poncelet n-gon!" or "Did not close in N steps").
- "Reset" button: clear construction, keep ellipses, wait for new click.

---

## UI layout (updated from current)

```
[ Conic A input ]   [ Conic B input ]   [ Draw ]  [ Reset ]

[ canvas 420x420                    ]   [ status / result text ]
```

Status div shows:
- "Click a point on the outer ellipse to start" (after Draw)
- "Building construction…" (during animation)
- "Poncelet 3-gon! (triangle)" / "Poncelet 5-gon!" etc.
- "Did not close within 10 steps."
- Warning if inputs are invalid.

---

## Implementation order
1. Step 1 (validation) — test with default inputs
2. Step 2 (snap to A) — test click → dot appears on ellipse
3. Step 3 (polar / tangent points) — test: draw two tangent points from a clicked P
4. Step 4 (one Poncelet step) — test: draw one tangent line + next point
5. Steps 5–6 (full loop + static draw)
6. Step 7 (animation)
