"""Test the translators for geometry to Gem."""
from ladybug_geometry.geometry3d import Point3D, Face3D
from dragonfly.model import Model
from dragonfly.building import Building
from dragonfly.story import Story
from dragonfly.room2d import Room2D
from dragonfly.roof import RoofSpecification
from dragonfly.windowparameter import SimpleWindowRatio

from dragonfly_iesve.writer import model_to_gem


def test_model_to_inp():
    """Test translating a Dragonfly Model to an inp file."""
    # Crate an input Model
    pts1 = (Point3D(0, 0, 0), Point3D(10, 0, 0),
            Point3D(10, 10, 0), Point3D(0, 10, 0))
    pts2 = (Point3D(10, 0, 0), Point3D(20, 0, 0),
            Point3D(20, 10, 0), Point3D(10, 10, 0))
    pts3 = (Point3D(0, 0, 3.25), Point3D(20, 0, 3.25),
            Point3D(20, 5, 5), Point3D(0, 5, 5))
    pts4 = (Point3D(0, 5, 5), Point3D(20, 5, 5),
            Point3D(20, 10, 3.25), Point3D(0, 10, 3.25))
    room2d_full = Room2D(
        'R1-full', floor_geometry=Face3D(pts1), floor_to_ceiling_height=4,
        is_ground_contact=True, is_top_exposed=True)
    room2d_plenum = Room2D(
        'R2-plenum', floor_geometry=Face3D(pts2), floor_to_ceiling_height=4,
        is_ground_contact=True, is_top_exposed=True)
    room2d_plenum.ceiling_plenum_depth = 1.0
    roof = RoofSpecification([Face3D(pts3), Face3D(pts4)])
    story = Story('S1', [room2d_full, room2d_plenum])
    story.roof = roof
    story.solve_room_2d_adjacency(0.01)
    story.set_outdoor_window_parameters(SimpleWindowRatio(0.4))
    building = Building('Office_Building_1234', [story])
    model = Model('NewDevelopment1', [building])

    # create the INP string for the model
    gem_str = model_to_gem(model)
    assert len(gem_str) > 1000


def test_vertical_air_boundary():
    """Test the translation of a Model to GEM with a vertical air boundary."""
    input_df_model = './tests/assets/vertical_connection.dfjson'
    model = Model.from_file(input_df_model)
    gem_str = model_to_gem(model)

    assert '42 2\n' in gem_str
