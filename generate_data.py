import argparse
import os
import numpy as np
#import torch

#from utils.data_utils import check_extension, save_dataset

# Check if a GPU is available
#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


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
            "n_Fis": n_fishers,
            "n_Aqua": n_aquaculture_farmers,
            "n_pro_unt": n_processing_units,
            "n_can_fac": n_canning_factories,
            "n_who": n_wholesalers,
            "n_col": n_collectors,
            "n_sea_mar1": n_seafood_market1,
            "n_sea_mar2": n_seafood_market2,
            "n_customers": n_seafood_market1 + n_seafood_market2,
            "n_wst_powd_fact": n_waste_powder_factories,
            "n_rev_cus": n_reverse_customers,
            # Parameters of Problem
            # Fixed costs
            "Fc_pro_unt_i": np.random.uniform(0, 1,processing_units),  # Fixed cost of opening processing unit i
            "Fc_can_fac_i": np.random.uniform(0, 1, n_canning_factories),  # Fixed cost of canning factory unit i
            "Fc_who_i": np.random.uniform(0,1,n_wholesalers),  # Fixed cost of opening wholesaler unit i
            "Fc_col_i": np.random.uniform(0,1,n_collectors),  # Fixed cost of opening collector unit i
            "Fc_wst_powd_fac_i": np.random.uniform(0,1,n_waste_powder_factories),  # Fixed cost of opening waste powder factory unit i
            # Transportation cost costs
            "Tc_fisher_to_processing_unit_i" : np.random.uniform(0, 1 , (n_fishers, n_processing_units)),
            "Tc_fisher_to_facotry_i" : np.random.uniform(0, 1 , (n_fishers, n_processing_units)) ,
            "Tc_aqua_farmer_to_processing_unit_i" : np.random.uniform(0, 1 , (n_fishers, n_processing_units)),
            "Tc_aqua_farmer_to_processing_factory_i" : np.random.uniform(0, 1 , (n_fishers, n_processing_units)) ,
            "Tc_fisher_processing_unit_i" : np.random.uniform(0, 1 , (n_fishers, n_processing_units)) ,
            "Tc_fisher_processing_unit_i" : np.random.uniform(0, 1 , (n_fishers, n_processing_units)) ,
            "Tc_fisher_processing_unit_i" : np.random.uniform(0, 1 , (n_fishers, n_processing_units)) ,
            "Tc_fisher_processing_unit_i : np.random.uniform(0, 1 , (n_fishers, n_processing_units)) ,
            "Tc_fisher_processing_unit_i" : np.random.uniform(0, 1 , (n_fishers, n_processing_units)) ,
            "Tc_fisher_processing_unit_i" : np.random.uniform(0, 1 , (n_fishers, n_processing_units)) ,
            "Tc_fisher_processing_unit_i" : np.random.uniform(0, 1 , (n_fishers, n_processing_units)) ,
            "Tc_fisher_processing_unit_i" : np.random.uniform(0, 1 , (n_fishers, n_processing_units)) ,
            "Tc_fisher_processing_unit_i" : np.random.uniform(0, 1 , (n_fishers, n_processing_units)) ,
            "Tc_fisher_processing_unit_i" : np.random.uniform(0, 1 , (n_fishers, n_processing_units)) ,
            "Tc_fisher_processing_unit_i" : np.random.uniform(0, 1 , (n_fishers, n_processing_units)) 
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
