import pytest

from qa_scripts.visual_regression import compare_pixel_buffers


def test_visual_regression_passes_under_threshold():
    result = compare_pixel_buffers([1, 1, 1, 1], [1, 1, 1, 2], threshold=0.25)
    assert result.passed is True
    assert result.changed_pixels == 1


def test_visual_regression_rejects_mismatched_buffers():
    with pytest.raises(ValueError, match="same pixel count"):
        compare_pixel_buffers([1], [1, 2])


def test_visual_regression_rejects_invalid_threshold():
    with pytest.raises(ValueError, match="between 0 and 1"):
        compare_pixel_buffers([1], [1], threshold=1.5)
