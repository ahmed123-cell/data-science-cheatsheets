"""NVIDIA Triton Python gRPC Inference Client (triton_client.py).

Demonstrates calling Triton Inference Server over high-speed binary gRPC.
"""

import numpy as np

try:
    import tritonclient.grpc as grpcclient
    HAS_TRITON_CLIENT = True
except ImportError:
    HAS_TRITON_CLIENT = False


def call_triton_server(server_url: str = "localhost:8001", model_name: str = "ride_duration_onnx"):
    """Sends inference request to Triton over gRPC."""
    if not HAS_TRITON_CLIENT:
        print("tritonclient is not installed. Run 'pip install tritonclient[all]' to enable.")
        # Fallback simulation
        print(f"[Simulated] Connected to Triton gRPC server at {server_url} for model '{model_name}'")
        dummy_input = np.array([[43.0, 142.0, 3.5, 1.0, 14.0, 2.0]], dtype=np.float32)
        print("Sent input shape:", dummy_input.shape)
        dummy_output = np.array([[13.25]], dtype=np.float32)
        print("Received prediction from Triton:", dummy_output[0][0], "minutes (latency: 1.2 ms)")
        return dummy_output

    with grpcclient.InferenceServerClient(url=server_url) as client:
        # Check server readiness
        if not client.is_server_ready():
            raise RuntimeError(f"Triton server at {server_url} is not ready.")

        # Prepare input tensor
        input_data = np.array([[43.0, 142.0, 3.5, 1.0, 14.0, 2.0]], dtype=np.float32)
        inputs = [grpcclient.InferInput("float_input", input_data.shape, "FP32")]
        inputs[0].set_data_from_numpy(input_data)

        # Execute call
        results = client.infer(model_name=model_name, inputs=inputs)
        output_data = results.as_numpy("variable")
        print("Triton gRPC prediction:", output_data)
        return output_data


if __name__ == "__main__":
    call_triton_server()
