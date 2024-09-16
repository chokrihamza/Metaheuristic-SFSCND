import pandas as pd
import geopandas
import folium
import random

random.seed(45)


def add_geocoordinates(df, lat="lat", lon="lon"):
    """
    Add column "geometry" with <shapely.geometry.point.Point> objects
        built from latitude and longitude values in the input dataframe
    """
    assert (
        pd.Series([lat, lon]).isin(df.columns).all()
    ), f'Cannot find columns "{lat}" and/or "{lon}" in the input dataframe.'
    return geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.lon, df.lat))


def plot_data(
    fisher_df,
    farmer_df,
    canning_factory_df,
    processing_unit_df,
    wholesaler_df,
    market_df,
    collector_center_df,
    waste_factory_df,
    reverse_market_df,
):
    # Create a Folium map centered around France
    m = folium.Map(location=[50, 2], zoom_start=7)

    # Add markers for each data point
    for df, color, label in zip(
        [
            fisher_df,
            farmer_df,
            canning_factory_df,
            processing_unit_df,
            wholesaler_df,
            market_df,
            collector_center_df,
            waste_factory_df,
            reverse_market_df,
        ],
        [
            "pink",
            "green",
            "white",
            "cadetblue",
            "purple",
            "red",
            "beige",
            "orange",
            "lightgreen",
        ],
        [
            "Fisher",
            "Farmer",
            "Factory",
            "Processing Unit",
            "Wholesaler",
            "Client",
            "Collector Center",
            "Waste Factory",
            "Poultry Market",
        ],
    ):

        for index, row in df.iterrows():
            folium.Marker(
                location=[row["lat"], row["lon"]],  # Assuming correct column names
                popup=row["name"],
                icon=folium.Icon(color=color, icon="info-sign"),
            ).add_to(m)

    return m


def generate_transportation_costs(source, destination, min_val, max_val):
    """
    transporation_costs = {}

    # For each warehouse location
    for i in range(0, source.shape[0]):
        costs = {}
        for j in range(0, destination.shape[0]):

            costs.update(
                {destination.processing_unit_id[j]: random.randint(min_val, max_val)}
            )

        # Final dictionary with all costs for all warehouses
        transporation_costs.update({source.fisher_id[i]: costs})
    """
