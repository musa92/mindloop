# Brain Component Architecture

MindLoop organizes the brain into modular components. Each component can be trained independently for the tasks that require it. For example, heavy motor tasks can focus on training the `MotorCortex` while planning intensive tasks target the `PrefrontalCortex`.

## Components
- **MotorCortex** – handles low level motor control.
- **PrefrontalCortex** – responsible for high level planning.

Components are registered in a central `Brain` object which orchestrates training across modules.
