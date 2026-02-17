import sys
import os

def test_best_paper_resurrection():
    try:
        # 1. THE NAMESPACE TRIPWIRE
        # In 2017, DenseNet relied on these specific sub-modules.
        # In 2026 (Keras 3.x), these throw an ImportError immediately.
        import keras
        from keras.models import Model
        from keras.layers import Input, Conv2D, Dense, AveragePooling2D
        import keras.utils.generic_utils as generic_utils 
        
        # 2. THE FUNCTIONAL API TRIPWIRE
        # Legacy Keras used 'merge' or 'concatenate' differently than Keras 3.
        from keras.layers import concatenate
        
        # Mock a small DenseNet-style connection
        input_shape = (32, 32, 3)
        img_input = Input(shape=input_shape)
        x = Conv2D(64, (3, 3), padding='same')(img_input)
        y = Conv2D(64, (3, 3), padding='same')(x)
        z = concatenate([x, y])
        
        print(f"✅ Validation Passed: CVPR 2017 Architecture initialized (Keras {keras.__version__})")
        return True
        
    except (ImportError, AttributeError, ModuleNotFoundError) as e:
        # This will be the "Attack" result (Red)
        print(f"❌ Validation Failed: Zero-Manifest Dependency Break. {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Validation Failed: {type(e).__name__}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_best_paper_resurrection()