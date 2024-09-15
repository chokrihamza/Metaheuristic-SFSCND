import argparse
import os
import numpy as np

# import torch

# from utils.data_utils import check_extension, save_dataset

# Check if a GPU is available
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# Data generator for seafood supply chain network design
def generate_MCLP_data(
    n_samples,
    n_fishers,
    n_aquaculture_farmers,
    n_processing_units,
    n_canning_factories,
    n_wholesalers,
    n_seafood_market1,
    n_seafood_market2,
    n_collectors,
    n_waste_powder_factories,
    n_reverse_customers,
):

    data = [
        {
            "n_i": n_fishers,
            "n_j": n_aquaculture_farmers,
            "n_k": n_processing_units,
            "n_l": n_canning_factories,
            "n_m": n_wholesalers,
            "n_n": n_collectors,
            "n_p": n_seafood_market1,
            "n_p_prime": n_seafood_market2,
            "n_customers": n_seafood_market1 + n_seafood_market2,
            "n_o": n_waste_powder_factories,
            "n_q": n_reverse_customers,
            "n_q_prime": n_reverse_customers,
            "n_rev": n_reverse_customers,
            # Parameters of Problem
            # Fixed costs
            "fi": np.random.uniform(
                0, 1, n_processing_units
            ),  # Fixed cost of opening processing unit i
            "fl": np.random.uniform(
                0, 1, n_canning_factories
            ),  # Fixed cost of canning factory unit l
            "fm": np.random.uniform(
                0, 1, n_wholesalers
            ),  # Fixed cost of opening wholesaler unit m
            "fn": np.random.uniform(
                0, 1, n_collectors
            ),  # Fixed cost of opening collector unit n
            "fo": np.random.uniform(
                0, 1, n_waste_powder_factories
            ),  # Fixed cost of opening waste powder factory unit o
            # Transportation costs
            "tpik": np.random.uniform(0, 1, (n_fishers, n_processing_units)),
            "tpil": np.random.uniform(0, 1, (n_fishers, n_canning_factories)),
            "tpjk": np.random.uniform(
                0, 1, (n_aquaculture_farmers, n_processing_units)
            ),
            "tpjl": np.random.uniform(
                0, 1, (n_aquaculture_farmers, n_canning_factories)
            ),
            "tpik": np.random.uniform(0, 1, (n_processing_units, n_wholesalers)),
            "tpik": np.random.uniform(0, 1, (n_canning_factories, n_wholesalers)),
            "tpik": np.random.uniform(
                0, 1, (n_wholesalers, n_seafood_market1 + n_seafood_market2)
            ),
            "tpik": np.random.uniform(
                0, 1, (n_seafood_market1 + n_seafood_market2, n_collectors)
            ),
            "tpik": np.random.uniform(0, 1, (n_fishers, n_processing_units)),
            "tpik": np.random.uniform(0, 1, (n_fishers, n_processing_units)),
            "tpik": np.random.uniform(0, 1, (n_fishers, n_processing_units)),
            "tpik": np.random.uniform(0, 1, (n_fishers, n_processing_units)),
            "tpik": np.random.uniform(0, 1, (n_fishers, n_processing_units)),
            "tpik": np.random.uniform(0, 1, (n_fishers, n_processing_units)),
            "tpik": np.random.uniform(0, 1, (n_fishers, n_processing_units)),
        }
        for _ in range(n_samples)
    ]

    return data


print(
    generate_MCLP_data(
        n_samples=10,
        n_fishers=10,
        n_aquaculture_farmers=12,
        n_processing_units=14,
        n_canning_factories=13,
        n_wholesalers=10,
        n_seafood_market1=5,
        n_seafood_market2=12,
        n_collectors=10,
        n_waste_powder_factories=12,
        n_reverse_customers=13,
    )
)
