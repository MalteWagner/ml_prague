import os
import tensorflow as tf
from train import get_default_hyperparams, train_and_evaluate, _reset_seeds
from models import Baseline_mb, Baseline_cbr_mb

# Set up training parameters
ds_path = "data\gnnet-ch23-dataset-cbr-mb-prepped_cv"  # Path to the dataset
hyperparams = get_default_hyperparams()

epochs = 5
optimizer = hyperparams["optimizer"]
loss = hyperparams["loss"]
metrics = hyperparams["metrics"]
additional_callbacks = hyperparams["additional_callbacks"]
folds = False

if __name__ == "__main__":
    if folds:
        # Add k-Fold Code
        pass
    else:    
        _reset_seeds()
        
        # Call train_and_evaluate function
        trained_model, evaluation = train_and_evaluate(
            ds_path=os.path.join(ds_path, "0"),
            model=Baseline_cbr_mb(),
            optimizer=optimizer,
            loss=loss,
            metrics=metrics,
            additional_callbacks=additional_callbacks,
            epochs=epochs,
        )

    # Print final evaluation
    print("Final evaluation:", evaluation)