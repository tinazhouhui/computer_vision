"""
Routing correct arguments to start correct functions
"""
from image_analysis.coin_recognition import circle_coins, compare_circle_detection
from image_processing.bitwise_operations import bitwise
from image_processing.blend import blend
from image_processing.convo import create_transformed_outputs, edge_detection
from image_processing.gamma import gamma_correction


def router(argument):
    """
    takes the argument from the system and starts the correct file
    """
    routes = {
        'convolution': create_transformed_outputs,
        'edge-detection': edge_detection,
        'blend': blend,
        'bitwise-operations': bitwise,
        'gamma-correction': gamma_correction,
        'coin-detection': compare_circle_detection,
    }

    return routes[argument]
