# test_renderpen.py
import pytest
from renderpen import RenderPen

@pytest.fixture
def rp():
    return RenderPen()

# --- Тести validate_upload ---

def test_upload_valid(rp):
    # AAA: Arrange, Act, Assert
    res = rp.validate_upload("test.glb", 10.0) # EP: Позитивний
    assert res is True

def test_upload_invalid_ext(rp):
    with pytest.raises(ValueError):
        rp.validate_upload("test.txt", 10.0) # EP: Негативний

def test_upload_boundary_max(rp):
    assert rp.validate_upload("test.glb", 50.0) is True # BVA: Межа

def test_upload_exceed_max(rp):
    assert rp.validate_upload("test.glb", 50.1) is False # BVA: Межа + 0.1

def test_upload_zero_size(rp):
    with pytest.raises(ValueError):
        rp.validate_upload("test.glb", 0) # BVA: Межа

# --- Тести validate_label ---

def test_label_valid(rp):
    assert rp.validate_label(0, 0, 0, "Двигун") is True # EP

def test_label_out_of_bounds(rp):
    assert rp.validate_label(1000.1, 0, 0, "Error") is False # BVA

def test_label_too_long(rp):
    assert rp.validate_label(0, 0, 0, "A" * 101) is False # BVA

def test_label_empty(rp):
    assert rp.validate_label(0, 0, 0, "   ") is False # EP: Негативний

# --- Тести format_public_link ---

def test_link_published(rp):
    assert "https://" in rp.format_public_link("proj1", True) # EP

def test_link_private(rp):
    assert rp.format_public_link("proj1", False) == "Project is private" # EP

def test_link_empty_id(rp):
    with pytest.raises(ValueError):
        rp.format_public_link("", True) # EP: Негативний
        