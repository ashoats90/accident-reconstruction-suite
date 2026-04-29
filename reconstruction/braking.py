import numpy as np 

def speed_from_skid(
        skid_distance_ft: float,
        drag_factor: float,
        braking_efficiency: float = 1.0,
        road_grade: float = 0.0
) -> float:
    
    effective_drag = drag_factor * braking_efficiency + road_grade

    if skid_distance_ft <=0:
        raise ValueError("Skid distance must be positive.")
    if drag_factor <= 0:
        raise ValueError("Drag factor must be positive.")
    if not 0 < braking_efficiency <= 1:
        raise ValueError("Braking efficiency must be between 0 and 1.")
    if effective_drag <= 0:
        raise ValueError("Effective drag must be positive.")
    
    return np.sqrt(30 * skid_distance_ft * effective_drag)