
module GenomeToPowerpointConverter {

    typedef structure {
        string genome_ref;
        string pp_theme;
    } G2PPparams;

    funcdef genome_to_powerpoint() returns (string pp_filename) authentication required;


    typedef structure {
        string pp_filename;
    } PP2Gparams;

    funcdef powerpoint_to_genome() returns (string genome_ref) authentication required;

};