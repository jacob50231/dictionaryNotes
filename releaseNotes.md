* Altered `submitted_unaligned_reads` Entity
	* Changes made to `properties`
		* Changes made to `read_pair_number`
			* Dropped Enumeration: `I1`
* Altered `annotation` Entity
	* Changes made to `links`
		* `copy_number_estimates` added to subgroup
	* Changes made to `properties`
		* New property: `copy_number_estimates`
* Altered `follow_up` Entity
	* Changes made to `properties`
		* New property: `hormonal_contraceptive_type`
		* New property: `hormone_replacement_therapy_type`
		* New property: `procedures_performed`
		* Changes made to `aids_risk_factors`
			* New permissable value: `Cryptosporidiosis, Chronic Intestinal`
		* Changes made to `comorbidity`
			* New permissable value: `Ataxia-telangiectasia`
			* New permissable value: `Autoimmune Lymphoproliferative Syndrome (ALPS)`
			* New permissable value: `Bacteroides fragilis`
			* New permissable value: `Chlamydia`
			* New permissable value: `Chronic Systemic Steroid Use`
			* New permissable value: `Cryptococcal Meningitis`
			* New permissable value: `Cytomegalovirus (CMV)`
			* New permissable value: `Lymphocytic Meningitis`
			* New permissable value: `Malaria`
			* New permissable value: `Metabolic Syndrome`
			* New permissable value: `Mycobacterium avium Complex`
			* New permissable value: `Pneumocystis Pneumonia`
			* New permissable value: `Polycystic Ovarian Syndrome (PCOS)`
			* New permissable value: `Shingles`
			* New permissable value: `Sjogren's Syndrome`
			* New permissable value: `Staphylococcus aureus`
			* New permissable value: `Syphilis`
			* New permissable value: `Treponema pallidum`
		* Changes made to `evidence_of_recurrence_type`
			* New permissable value: `Physical Examination`
		* Changes made to `risk_factor`
			* New permissable value: `Ataxia-telangiectasia`
			* New permissable value: `Autoimmune Lymphoproliferative Syndrome (ALPS)`
			* New permissable value: `Bacteroides fragilis`
			* New permissable value: `BAP1 Tumor Predisposition Syndrome`
			* New permissable value: `Birt-Hogg-Dube Syndrome`
			* New permissable value: `Chlamydia`
			* New permissable value: `Chronic Systemic Steroid Use`
			* New permissable value: `Cowden Syndrome`
			* New permissable value: `Cryptococcal Meningitis`
			* New permissable value: `Cytomegalovirus (CMV)`
			* New permissable value: `Hereditary Breast Cancer`
			* New permissable value: `Hereditary Kidney Oncocytoma`
			* New permissable value: `Hereditary Leiomyomatosis and Renal Cell Carcinoma`
			* New permissable value: `Hereditary Ovarian Cancer`
			* New permissable value: `Hereditary Papillary Renal Cell Carcinoma`
			* New permissable value: `Hereditary Renal Cell Carcinoma`
			* New permissable value: `Lymphocytic Meningitis`
			* New permissable value: `Malaria`
			* New permissable value: `Metabolic Syndrome`
			* New permissable value: `Mycobacterium avium Complex`
			* New permissable value: `Pneumocystis Pneumonia`
			* New permissable value: `Polycystic Ovarian Syndrome (PCOS)`
			* New permissable value: `Shingles`
			* New permissable value: `Sjogren's Syndrome`
			* New permissable value: `Staphylococcus aureus`
			* New permissable value: `Succinate Dehydrogenase-Deficient Renal Cell Carcinoma`
			* New permissable value: `Syphilis`
			* New permissable value: `Treponema pallidum`
			* New permissable value: `Tuberculosis`
			* New permissable value: `Tuberous Sclerosis`
			* New permissable value: `Von Hippel-Lindau Syndrome`
* Altered `read_group` Entity
	* Changes made to `properties`
		* New property: `chipseq_target`
* Altered `sample` Entity
	* New property: `deprecated`
	* Changes made to `properties`
		* Changes made to `sample_type`
			* New permissable value: `Mixed Adherent Suspension`
			* New permissable value: `Saliva`
* Altered `analyte` Entity
	* Changes made to `properties`
		* Changes made to `analyte_type`
			* New permissable value: `Nuclei RNA`
* Altered `exposure` Entity
	* Changes made to `properties`
		* New property: `alcohol_type`
		* New property: `smokeless_tobacco_quit_age`
		* Changes made to `exposure_type`
			* New permissable value: `Smoke`
			* New permissable value: `Wood Dust`
		* Changes made to `type_of_smoke_exposure`
			* New permissable value: `Tobacco smoke, NOS`
* New Entity: `pathology_detail`
* Altered `diagnosis` Entity
	* Changes made to `required`
		* Dropped Item: `days_to_last_follow_up`
		* Dropped Item: `tumor_grade`
		* Dropped Item: `progression_or_recurrence`
		* Dropped Item: `days_to_recurrence`
		* Dropped Item: `days_to_last_known_disease_status`
		* Dropped Item: `last_known_disease_status`
	* Changes made to `deprecated`
		* New Item: `micropapillary_features`
		* New Item: `mitotic_count`
		* New Item: `non_nodal_regional_disease`
		* New Item: `non_nodal_tumor_deposits`
		* New Item: `papillary_renal_cell_type`
	* Changes made to `properties`
		* New property: `eln_risk_classification`
		* New property: `satellite_nodule_present`
		* New property: `sites_of_involvement`
		* New property: `who_cns_grade`
		* New property: `who_nte_grade`
		* Changes made to `ajcc_pathologic_stage`
			* New permissable value: `Stage IA3`
		* Changes made to `classification_of_tumor`
			* New permissable value: `Progression`
		* Changes made to `metastasis_at_diagnosis_site`
			* New permissable value: `Esophagus`
		* Changes made to `morphology`
			* New permissable value: `8040/3`
			* New permissable value: `8046/6`
			* New permissable value: `8240/6`
			* New permissable value: `8471/1`
			* New permissable value: `8500/6`
			* New permissable value: `8720/6`
			* New permissable value: `8801/6`
			* New permissable value: `8804/6`
			* New permissable value: `8920/6`
			* New permissable value: `8950/6`
			* New permissable value: `9180/6`
			* New permissable value: `9440/6`
		* Changes made to `site_of_resection_or_biopsy`
			* New permissable value: `Pancreatic neck`
* Altered `treatment` Entity
	* Changes made to `properties`
		* Changes made to `therapeutic_agents`
			* New permissable value: `ALK Inhibitor`
			* New permissable value: `CDK4/6 Inhibitor`
			* New permissable value: `IGF-1R Inhibitor`
			* New permissable value: `Itraconazole`
			* New permissable value: `PD-1 Inhibitor`
			* New permissable value: `Progestational IUD`
			* New permissable value: `Tipiracil`
			* New permissable value: `Tipiracil Hydrochloride`
			* New permissable value: `Zirconium Zr 89 Panitumumab`
		* Changes made to `therapeutic_agents`
			* Changes made to `deprecated_enum`
				* Dropped Item: `Folic Acid`
* Altered `rna_expression_workflow` Entity
	* Changes made to `properties`
		* Changes made to `workflow_type`
			* New permissable value: `STAR - Smart-Seq2 Gene Counts`
			* New permissable value: `STAR - Smart-Seq2 GeneFull Counts`
			* Dropped Enumeration: `STAR - Smart-Seq2 Counts`
* Altered `molecular_test` Entity
	* Changes made to `properties`
		* New property: `biospecimen_volume`
		* New property: `mitotic_count`
		* New property: `mitotic_total_area`
		* Changes made to `antigen`
			* New permissable value: `Prostate-Specific Antigen (PSA)`
		* Changes made to `gene_symbol`
			* New permissable value: `HOXB1`
		* Changes made to `laboratory_test`
			* New permissable value: `5-Hydroxyindoleacetic Acid`
			* New permissable value: `Chromogranin A`
			* New permissable value: `Chromogranin B`
			* New permissable value: `Gamma-Enolase`
		* Changes made to `second_gene_symbol`
			* New permissable value: `HOXB1`
