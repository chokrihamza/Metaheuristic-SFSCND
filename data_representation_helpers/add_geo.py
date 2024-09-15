import pandas as pd
import geopandas


def add_geocoordinates(df, lat="lat", lon="lon"):
    """
    Add column "geometry" with <shapely.geometry.point.Point> objects
        built from latitude and longitude values in the input dataframe
    """
    assert (
        pd.Series([lat, lon]).isin(df.columns).all()
    ), f'Cannot find columns "{lat}" and/or "{lon}" in the input dataframe.'
    return geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.lon, df.lat))
