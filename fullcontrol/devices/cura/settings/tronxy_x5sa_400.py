default_initial_settings = {
    "name": "Tronxy X5SA/X5ST/Pro/2E 400mm",
    "manufacturer": "Tronxy",
    "start_gcode": "; X5SA Start Code\nG21 ; Set units to millimeters\nG90 ; Set all axis to Absolute\nM82 ; Set extrusion to Absolute\nM107 ; Disable all fans\nM190 S{data['bed_temp']} ; Set bed temperature and wait\nG28 ; Home all axis\n; Uncomment the line below to enable ABL Mesh probing\n;G29 ; Probe bed mesh for ABL\n; For best results do not run nozzle heater while performing ABL\nG1 Z5.0 ; Raise nozzle to prevent scratching of heat bed\nG1 X0 Y0 ; Move nozzle to Home before heating\nM109 S{data['nozzle_temp']} T0 ; Set nozzle temp and wait\nG92 E0 ; Set Extruder position to zero\n; Uncomment the following lines to enable nozzle purge line along left edge of bed\n;G1 Z2.0 F3000 ; Raise Z axis\n;G1 X1.1 Y20 Z0.2 F3600.0 ; Move to purge line start position\n;G1 Y290 F1500.0 E15 ; Draw first purge line\n;G1 X1.4 F3600.0 ; Move to side\n;G1 Y20 F1500.0 E30 ; Draw second purge line\n;G92 E0 ; Reset Extruder\n;G1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed\n;G1 X5 Y20 Z0.2 F3600.0 ; Move over to finish nozzle wipe\n;G92 E0\n",
    "end_gcode": "G91 ; Set Positioning to Relative\nM83 ; Set Extruder to Relative\nG92 E0 ; Reset Extruder\nG1 E-4 F3000 ; Retract 4mm of filament\nG1 Z0.2 ; Raise nozzle .2mm\nG90 ; Set positioning to absolute\nG1 X{data['build_volume_x']} Y{data['build_volume_y']} ; Park print head\nG91 ; Set Positioning to RelativeG1 Z10 ; Raise nozzle 10mm\nM106 S0 ; Turn off part fan\nM104 S0 ; Set nozzle temp to zero\nM140 S0 ; set bed temp to zero\nM84 X Y Z E ; Disable X Y Z and E steppers\n",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 95,
    "print_speed": 60.0,
    "travel_speed": 75.0,
    "dia_feed": 1.75,
    "build_volume_x": 400,
    "build_volume_y": 400,
    "build_volume_z": 400,
}