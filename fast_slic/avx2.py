from cfast_slic import SlicModelAvx2, slic_supports_arch
from .base_slic import BaseSlic

if not slic_supports_arch("avx2"):
    raise ImportError(
        "fast_slic is not configured with avx2 support. "
        "Compile it again with flag USE_AVX2."
    )

class SlicAvx2(BaseSlic):
    def __init__(self, num_components=None, slic_model=None, compactness_shift=10, quantize_level=6):
        super().__init__(
            num_components=num_components,
            slic_model=slic_model or SlicModel(num_components or 100),
            compactness_shift=compactness_shift,
            quantize_level=quantize_level,
        )

    def make_slic_model(self, num_components):
        return SlicModelAvx2(num_components)

