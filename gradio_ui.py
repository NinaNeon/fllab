import io
import sys
import time
import threading
import subprocess
import gradio as gr


# Function to launch TensorBoard in the background
def launch_tensorboard(log_dir, port=6006):
    def run_tensorboard():
        subprocess.run(["tensorboard", "--logdir", log_dir, "--port", str(port)])
        
    thread = threading.Thread(target=run_tensorboard, daemon=True)
    thread.start()
    time.sleep(2)  # Wait for TensorBoard to start


def launch_gradio_ui(main_function, args):
    """
    Launches the Gradio UI for configuring training parameters and starting training.

    Args:
        args: The argparse.Namespace object containing default arguments.
        main_function: The function to call when the user starts training.
    """

    # Create Gradio components dynamically
    with gr.Blocks() as demo:
        gr.Markdown("# Federated Learning GUI")
        
        # Layout with two columns for separated sections
        with gr.Column():
            gr.Markdown("## FL Setting")
            with gr.Row():
                fl_inputs1 = {
                    "algorithm": gr.Dropdown(
                        choices=["fedavg", "fedprox", "scaffold", "fedmd", "feddf", "fedgen", "moon", "fedproto", "fpl", "flwf", "cfed", "fedcl"],
                        value="fedavg", 
                        label="Algorithm",
                    ),
                    "dataset": gr.Dropdown(
                        choices=["Mnist", "Cifar10", "Digits", "Office-Caltech"],
                        value="Mnist",
                        label="Dataset"
                    ),
                    "skew_type": gr.Dropdown(choices=["label", "feature", "quantity"], value="label", label="Skew Type"),
                    "alpha": gr.Number(value=100.0, label="Alpha"),
                    "model": gr.Dropdown(
                        choices=["SimpleCNN", "MyCNN", "ResNet10"],
                        value="SimpleCNN",
                        label="Model"
                    ),
                    "batch_size": gr.Slider(32, 512, value=128, step=32, label="Batch Size"),
                    # "lr": gr.Slider(0.001, 0.1, value=0.01, step=0.001, label="Learning Rate"),
                }
            with gr.Row():
                fl_inputs2 = {
                    "num_clients": gr.Slider(1, 20, value=10, step=1, label="Number of Clients"),
                    "num_classes": gr.Slider(2, 20, value=10, step=1, label="Number of Classes"),
                    "num_rounds": gr.Slider(1, 20, value=10, step=1, label="Number of Rounds"),
                    "num_epochs": gr.Slider(1, 10, value=5, step=1, label="Number of Epochs"),
                }
        
            gr.Markdown("## Dynamic Setting")
            with gr.Row():
                dp_inputs = {
                    "dynamic_type": gr.Dropdown(choices=["static", "round-robin", "incremental-arrival", "incremental-departure", "random", "markov"], value="static", label="Dynamic Type"),
                    "round_start": gr.Number(value=1, label="Round Start"),
                    "initial_clients": gr.Slider(1, 20, value=5, step=1, label="Initial Clients"),
                    "interval": gr.Slider(5, 30, value=10, step=1, label="Interval"),
                    "overlap_clients": gr.Slider(1, 10, value=2, step=1, label="Overlap Clients"),
                    "dpfl": gr.Checkbox(value=False, label="Enable Knowledge Pool Module"),
                }


        # Combine all input components into a single list for click() callback
        args_name = list(fl_inputs1.keys()) + list(fl_inputs2.keys()) + list(dp_inputs.keys())
        args_value = list(fl_inputs1.values()) + list(fl_inputs2.values()) + list(dp_inputs.values())
        
        # Button and Output
        start_button = gr.Button("▶ Start Training")
        output = gr.Textbox(label="Training Progress")
        
        with gr.Row():
            launch_tensorboard(args.log_dir)                                # Launch TensorBoard in the background
            tensorboard_iframe = gr.HTML("<iframe src='http://127.0.0.1:6006' width='100%' height='700'></iframe>")

        # Simplified Gradio interface function
        def gradio_interface(*vals):
            kwargs = dict(zip(args_name, vals))
            # Dynamically update args with user inputs
            for key, value in kwargs.items():
                setattr(args, key, value)
            
            main_function(args)
            return f" Training complete! 🎉 Check TensorBoard for results."

        # Link button to function
        start_button.click(
            gradio_interface,
            inputs=args_value,
            outputs=[output]
        )

    # Launch the Gradio app
    demo.launch(share=True)
