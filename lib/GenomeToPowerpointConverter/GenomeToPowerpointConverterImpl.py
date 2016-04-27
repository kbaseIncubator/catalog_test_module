#BEGIN_HEADER
#END_HEADER


class GenomeToPowerpointConverter:
    '''
    Module Name:
    GenomeToPowerpointConverter

    Module Description:
    
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass

    def genome_to_powerpoint(self, ctx):
        # ctx is the context object
        # return variables are: pp_filename
        #BEGIN genome_to_powerpoint
        pp_filename = "out.ppx"
        #END genome_to_powerpoint

        # At some point might do deeper type checking...
        if not isinstance(pp_filename, basestring):
            raise ValueError('Method genome_to_powerpoint return value ' +
                             'pp_filename is not type basestring as required.')
        # return the results
        return [pp_filename]

    def powerpoint_to_genome(self, ctx):
        # ctx is the context object
        # return variables are: genome_ref
        #BEGIN powerpoint_to_genome
        genome_ref = "41201/1/1"
        #END powerpoint_to_genome

        # At some point might do deeper type checking...
        if not isinstance(genome_ref, basestring):
            raise ValueError('Method powerpoint_to_genome return value ' +
                             'genome_ref is not type basestring as required.')
        # return the results
        return [genome_ref]
