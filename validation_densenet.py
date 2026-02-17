import sys
import os

# Suppress warnings to keep the ASE report clean
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def test_densenet_functional_api():
    try:
        # THE TRIPWIRE
        # This exact import sequence is what kills 2017 code in 2026.
        # Standalone 'keras' 3.x (2026) has removed 'generic_utils'.
        import keras
        from keras.models import Model
        from keras.layers import Input, Conv2D, Dense, concatenate
        import keras.utils.generic_utils as generic_utils
        
        # Verify the Functional API (DenseNet's core)
        input_shape = (32, 32, 3)
        img_input = Input(shape=input_shape)
        x = Conv2D(64, (3, 3), padding='same')(img_input)
        y = Conv2D(64, (3, 3), padding='same')(x)
        
        # DenseNet is famous for these concatenations
        z = concatenate([x, y])
        
        print(f"✅ Validation Passed: DenseNet architecture initialized (Keras {keras.__version__})")
        return True
        
    except (ImportError, AttributeError, ModuleNotFoundError) as e:
        # This will be the "Attack" result (Red)
        print(f"❌ Validation Failed: Legacy Namespace Breach. {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Validation Failed: {type(e).__name__}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_densenet_functional_api()