# Luanguege_tor_turtle_graphics
This language only works for 90-degree turns!
SR (1 or 0) -> Tracer on or off
SS >0 -> Set the step size
SSP 1-100 -> Set the tracer speed
M U D L R -> Move up, then down, then left etc...
M U2 D3 L4 R5 -> Move up twice, right three times etc...
CF my function [ -> Create a function (spaces work)
M U D L R
M U2 D2 L2 R2
M U3 D3 L3 R3
]
F my function -> call function
P (U or D) -> Pen up or down
comments work in plain text as long as they don't contain a command as the first chars:
comment <- This will work
/M U comment <- This will work
M U comment <- This will cause an error
