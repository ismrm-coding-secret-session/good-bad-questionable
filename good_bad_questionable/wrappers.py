def the_almighty_wrapper(myobject, **kwargs):
    """ Meant to run a very complicated processing pipeline

    Parameters:
    -----------
    myobject: myclass,
        Your input data preloaded in our custom way. The pipeline used to start 
        with just the path to the data, but importing routine turned out 
        different so many times, we finally decided to separate I/O 
        (just kidding, only input) into a separate function.

    # Following are the options to control the workflow and special cases

    echo_time: array-like, optional
        (necessary for the processing) If given, overwrites the echo time 
        specified in the input ``myclass`` instance

    which_echo_to_use: str, {'even','odd','all'}, optional
        default: 'all'
    
    use_<this-very-special-thing>_index: int, optional
        I happened to work on a dataset which has this feature, so this flag 
        will forever hang around here

    method_to_do_X: str, {'cauchy-gauss', 'iterative_splitting'}, optional
        bla-bla, default: iterative_splitting
    correct_cauchy_gauss: bool, optional
        Since cauchy-gauss is inexact, apply the following workaround...

    save_intermediate: bool, default: True
        Defines if intermediate results must be saved to the disc.
    intermediate_folder: str, default: os.path.join(os.getcwd(), 'intermediate')
        Path to the intermediate results folder. 
    recompute_all: bool, default: True
        If True, all intermediate results, if found on the disc, 
        will be recomputed. To pick up the processing from an existing step, 
        set to False and place the data in the ``intermediate_folder``
    recompute_step_a: bool, default: True
    recompute_step_b: bool, default: True
    ...
    
    Lorem: ipsum, dolor sit amet, 
        consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
        exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    
    Duis: aute, irure dolor
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
        in culpa qui officia deserunt mollit anim id est laborum.

    Sed: ut, perspiciatis
        unde omnis iste natus error sit voluptatem accusantium doloremque
        laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore 
        veritatis et quasi architecto beatae vitae dicta sunt explicabo. 

    Nemo: enim, ipsam
        voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
        consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. 

    Neque: porro, quisquam est, 
        qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, 
        sed quia non numquam eius modi tempora incidunt ut labore et dolore 
        magnam aliquam quaerat voluptatem. 

    Ut: enim,
        ad minima veniam, quis nostrum exercitationem ullam corporis suscipit 
        laboriosam, nisi ut aliquid ex ea commodi consequatur?

    Quis: autem, vel
        eum iure reprehenderit qui in ea voluptate velit esse quam nihil 
        molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas 
        nulla pariatur?
    
    # Related to "de Finibus Bonorum et Malorum"

    At: vero, eos
        et accusamus et iusto odio dignissimos ducimus qui blanditiis
        praesentium voluptatum deleniti atque corrupti quos dolores et quas
        molestias excepturi sint occaecati cupiditate non provident, 

    similique: sunt, in culpa 
        qui officia deserunt mollitia animi, id est laborum et dolorum fuga. 
        Et harum quidem rerum facilis est et expedita distinctio. 
    
    Nam: libero, tempore, 
        cum soluta nobis est eligendi optio cumque nihil impedit quo minus id
        quod maxime placeat facere possimus, omnis voluptas assumenda est, 
        omnis dolor repellendus. 
    
    Temporibus: autem, quibusdam
        et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et 
        voluptates repudiandae sint et molestiae non recusandae. 
    
    Itaque: earum, 
        rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus 
        maiores alias consequatur aut perferendis doloribus asperiores repellat 
    
    Lorem: ipsum, dolor sit amet, 
        consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
        exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    
    Duis: aute, irure dolor
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
        in culpa qui officia deserunt mollit anim id est laborum.

    Sed: ut, perspiciatis
        unde omnis iste natus error sit voluptatem accusantium doloremque
        laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore 
        veritatis et quasi architecto beatae vitae dicta sunt explicabo. 

    Nemo: enim, ipsam
        voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
        consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. 

    Neque: porro, quisquam est, 
        qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, 
        sed quia non numquam eius modi tempora incidunt ut labore et dolore 
        magnam aliquam quaerat voluptatem. 

    Ut: enim,
        ad minima veniam, quis nostrum exercitationem ullam corporis suscipit 
        laboriosam, nisi ut aliquid ex ea commodi consequatur?

    Quis: autem, vel
        eum iure reprehenderit qui in ea voluptate velit esse quam nihil 
        molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas 
        nulla pariatur?
    
    # Related to "de Finibus Bonorum et Malorum"

    At: vero, eos
        et accusamus et iusto odio dignissimos ducimus qui blanditiis
        praesentium voluptatum deleniti atque corrupti quos dolores et quas
        molestias excepturi sint occaecati cupiditate non provident, 

    similique: sunt, in culpa 
        qui officia deserunt mollitia animi, id est laborum et dolorum fuga. 
        Et harum quidem rerum facilis est et expedita distinctio. 
    
    Nam: libero, tempore, 
        cum soluta nobis est eligendi optio cumque nihil impedit quo minus id
        quod maxime placeat facere possimus, omnis voluptas assumenda est, 
        omnis dolor repellendus. 
    
    Temporibus: autem, quibusdam
        et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et 
        voluptates repudiandae sint et molestiae non recusandae. 
    
    Itaque: earum, 
        rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus 
        maiores alias consequatur aut perferendis doloribus asperiores repellat 
    
    Lorem: ipsum, dolor sit amet, 
        consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
        exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    
    Duis: aute, irure dolor
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
        in culpa qui officia deserunt mollit anim id est laborum.

    Sed: ut, perspiciatis
        unde omnis iste natus error sit voluptatem accusantium doloremque
        laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore 
        veritatis et quasi architecto beatae vitae dicta sunt explicabo. 

    Nemo: enim, ipsam
        voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
        consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. 

    Neque: porro, quisquam est, 
        qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, 
        sed quia non numquam eius modi tempora incidunt ut labore et dolore 
        magnam aliquam quaerat voluptatem. 

    Ut: enim,
        ad minima veniam, quis nostrum exercitationem ullam corporis suscipit 
        laboriosam, nisi ut aliquid ex ea commodi consequatur?

    Quis: autem, vel
        eum iure reprehenderit qui in ea voluptate velit esse quam nihil 
        molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas 
        nulla pariatur?
    
    # Related to "de Finibus Bonorum et Malorum"

    At: vero, eos
        et accusamus et iusto odio dignissimos ducimus qui blanditiis
        praesentium voluptatum deleniti atque corrupti quos dolores et quas
        molestias excepturi sint occaecati cupiditate non provident, 

    similique: sunt, in culpa 
        qui officia deserunt mollitia animi, id est laborum et dolorum fuga. 
        Et harum quidem rerum facilis est et expedita distinctio. 
    
    Nam: libero, tempore, 
        cum soluta nobis est eligendi optio cumque nihil impedit quo minus id
        quod maxime placeat facere possimus, omnis voluptas assumenda est, 
        omnis dolor repellendus. 
    
    Temporibus: autem, quibusdam
        et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et 
        voluptates repudiandae sint et molestiae non recusandae. 
    
    Itaque: earum, 
        rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus 
        maiores alias consequatur aut perferendis doloribus asperiores repellat 
    
    Lorem: ipsum, dolor sit amet, 
        consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
        exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    
    Duis: aute, irure dolor
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
        in culpa qui officia deserunt mollit anim id est laborum.

    Sed: ut, perspiciatis
        unde omnis iste natus error sit voluptatem accusantium doloremque
        laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore 
        veritatis et quasi architecto beatae vitae dicta sunt explicabo. 

    Nemo: enim, ipsam
        voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
        consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. 

    Neque: porro, quisquam est, 
        qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, 
        sed quia non numquam eius modi tempora incidunt ut labore et dolore 
        magnam aliquam quaerat voluptatem. 

    Ut: enim,
        ad minima veniam, quis nostrum exercitationem ullam corporis suscipit 
        laboriosam, nisi ut aliquid ex ea commodi consequatur?

    Quis: autem, vel
        eum iure reprehenderit qui in ea voluptate velit esse quam nihil 
        molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas 
        nulla pariatur?
    
    # Related to "de Finibus Bonorum et Malorum"

    At: vero, eos
        et accusamus et iusto odio dignissimos ducimus qui blanditiis
        praesentium voluptatum deleniti atque corrupti quos dolores et quas
        molestias excepturi sint occaecati cupiditate non provident, 

    similique: sunt, in culpa 
        qui officia deserunt mollitia animi, id est laborum et dolorum fuga. 
        Et harum quidem rerum facilis est et expedita distinctio. 
    
    Nam: libero, tempore, 
        cum soluta nobis est eligendi optio cumque nihil impedit quo minus id
        quod maxime placeat facere possimus, omnis voluptas assumenda est, 
        omnis dolor repellendus. 
    
    Temporibus: autem, quibusdam
        et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et 
        voluptates repudiandae sint et molestiae non recusandae. 
    
    Itaque: earum, 
        rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus 
        maiores alias consequatur aut perferendis doloribus asperiores repellat 
    
    Lorem: ipsum, dolor sit amet, 
        consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
        exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    
    Duis: aute, irure dolor
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
        in culpa qui officia deserunt mollit anim id est laborum.

    Sed: ut, perspiciatis
        unde omnis iste natus error sit voluptatem accusantium doloremque
        laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore 
        veritatis et quasi architecto beatae vitae dicta sunt explicabo. 

    Nemo: enim, ipsam
        voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
        consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. 

    Neque: porro, quisquam est, 
        qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, 
        sed quia non numquam eius modi tempora incidunt ut labore et dolore 
        magnam aliquam quaerat voluptatem. 

    Ut: enim,
        ad minima veniam, quis nostrum exercitationem ullam corporis suscipit 
        laboriosam, nisi ut aliquid ex ea commodi consequatur?

    Quis: autem, vel
        eum iure reprehenderit qui in ea voluptate velit esse quam nihil 
        molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas 
        nulla pariatur?
    
    # Related to "de Finibus Bonorum et Malorum"

    At: vero, eos
        et accusamus et iusto odio dignissimos ducimus qui blanditiis
        praesentium voluptatum deleniti atque corrupti quos dolores et quas
        molestias excepturi sint occaecati cupiditate non provident, 

    similique: sunt, in culpa 
        qui officia deserunt mollitia animi, id est laborum et dolorum fuga. 
        Et harum quidem rerum facilis est et expedita distinctio. 
    
    Nam: libero, tempore, 
        cum soluta nobis est eligendi optio cumque nihil impedit quo minus id
        quod maxime placeat facere possimus, omnis voluptas assumenda est, 
        omnis dolor repellendus. 
    
    Temporibus: autem, quibusdam
        et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et 
        voluptates repudiandae sint et molestiae non recusandae. 
    
    Itaque: earum, 
        rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus 
        maiores alias consequatur aut perferendis doloribus asperiores repellat 
    
    Lorem: ipsum, dolor sit amet, 
        consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
        exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    
    Duis: aute, irure dolor
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
        in culpa qui officia deserunt mollit anim id est laborum.

    Sed: ut, perspiciatis
        unde omnis iste natus error sit voluptatem accusantium doloremque
        laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore 
        veritatis et quasi architecto beatae vitae dicta sunt explicabo. 

    Nemo: enim, ipsam
        voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
        consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. 

    Neque: porro, quisquam est, 
        qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, 
        sed quia non numquam eius modi tempora incidunt ut labore et dolore 
        magnam aliquam quaerat voluptatem. 

    Ut: enim,
        ad minima veniam, quis nostrum exercitationem ullam corporis suscipit 
        laboriosam, nisi ut aliquid ex ea commodi consequatur?

    Quis: autem, vel
        eum iure reprehenderit qui in ea voluptate velit esse quam nihil 
        molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas 
        nulla pariatur?
    
    # Related to "de Finibus Bonorum et Malorum"

    At: vero, eos
        et accusamus et iusto odio dignissimos ducimus qui blanditiis
        praesentium voluptatum deleniti atque corrupti quos dolores et quas
        molestias excepturi sint occaecati cupiditate non provident, 

    similique: sunt, in culpa 
        qui officia deserunt mollitia animi, id est laborum et dolorum fuga. 
        Et harum quidem rerum facilis est et expedita distinctio. 
    
    Nam: libero, tempore, 
        cum soluta nobis est eligendi optio cumque nihil impedit quo minus id
        quod maxime placeat facere possimus, omnis voluptas assumenda est, 
        omnis dolor repellendus. 
    
    Temporibus: autem, quibusdam
        et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et 
        voluptates repudiandae sint et molestiae non recusandae. 
    
    Itaque: earum, 
        rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus 
        maiores alias consequatur aut perferendis doloribus asperiores repellat 
    
    Lorem: ipsum, dolor sit amet, 
        consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
        exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    
    Duis: aute, irure dolor
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
        in culpa qui officia deserunt mollit anim id est laborum.

    Sed: ut, perspiciatis
        unde omnis iste natus error sit voluptatem accusantium doloremque
        laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore 
        veritatis et quasi architecto beatae vitae dicta sunt explicabo. 

    Nemo: enim, ipsam
        voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
        consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. 

    Neque: porro, quisquam est, 
        qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, 
        sed quia non numquam eius modi tempora incidunt ut labore et dolore 
        magnam aliquam quaerat voluptatem. 

    Ut: enim,
        ad minima veniam, quis nostrum exercitationem ullam corporis suscipit 
        laboriosam, nisi ut aliquid ex ea commodi consequatur?

    Quis: autem, vel
        eum iure reprehenderit qui in ea voluptate velit esse quam nihil 
        molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas 
        nulla pariatur?
    
    # Related to "de Finibus Bonorum et Malorum"

    At: vero, eos
        et accusamus et iusto odio dignissimos ducimus qui blanditiis
        praesentium voluptatum deleniti atque corrupti quos dolores et quas
        molestias excepturi sint occaecati cupiditate non provident, 

    similique: sunt, in culpa 
        qui officia deserunt mollitia animi, id est laborum et dolorum fuga. 
        Et harum quidem rerum facilis est et expedita distinctio. 
    
    Nam: libero, tempore, 
        cum soluta nobis est eligendi optio cumque nihil impedit quo minus id
        quod maxime placeat facere possimus, omnis voluptas assumenda est, 
        omnis dolor repellendus. 
    
    Temporibus: autem, quibusdam
        et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et 
        voluptates repudiandae sint et molestiae non recusandae. 
    
    Itaque: earum, 
        rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus 
        maiores alias consequatur aut perferendis doloribus asperiores repellat 
    
    Lorem: ipsum, dolor sit amet, 
        consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
        exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    
    Duis: aute, irure dolor
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
        in culpa qui officia deserunt mollit anim id est laborum.

    Sed: ut, perspiciatis
        unde omnis iste natus error sit voluptatem accusantium doloremque
        laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore 
        veritatis et quasi architecto beatae vitae dicta sunt explicabo. 

    Nemo: enim, ipsam
        voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
        consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. 

    Neque: porro, quisquam est, 
        qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, 
        sed quia non numquam eius modi tempora incidunt ut labore et dolore 
        magnam aliquam quaerat voluptatem. 

    Ut: enim,
        ad minima veniam, quis nostrum exercitationem ullam corporis suscipit 
        laboriosam, nisi ut aliquid ex ea commodi consequatur?

    Quis: autem, vel
        eum iure reprehenderit qui in ea voluptate velit esse quam nihil 
        molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas 
        nulla pariatur?
    
    # Related to "de Finibus Bonorum et Malorum"

    At: vero, eos
        et accusamus et iusto odio dignissimos ducimus qui blanditiis
        praesentium voluptatum deleniti atque corrupti quos dolores et quas
        molestias excepturi sint occaecati cupiditate non provident, 

    similique: sunt, in culpa 
        qui officia deserunt mollitia animi, id est laborum et dolorum fuga. 
        Et harum quidem rerum facilis est et expedita distinctio. 
    
    Nam: libero, tempore, 
        cum soluta nobis est eligendi optio cumque nihil impedit quo minus id
        quod maxime placeat facere possimus, omnis voluptas assumenda est, 
        omnis dolor repellendus. 
    
    Temporibus: autem, quibusdam
        et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et 
        voluptates repudiandae sint et molestiae non recusandae. 
    
    Itaque: earum, 
        rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus 
        maiores alias consequatur aut perferendis doloribus asperiores repellat 
    
    Lorem: ipsum, dolor sit amet, 
        consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
        exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    
    Duis: aute, irure dolor
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
        in culpa qui officia deserunt mollit anim id est laborum.

    Sed: ut, perspiciatis
        unde omnis iste natus error sit voluptatem accusantium doloremque
        laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore 
        veritatis et quasi architecto beatae vitae dicta sunt explicabo. 

    Nemo: enim, ipsam
        voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
        consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. 

    Neque: porro, quisquam est, 
        qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, 
        sed quia non numquam eius modi tempora incidunt ut labore et dolore 
        magnam aliquam quaerat voluptatem. 

    Ut: enim,
        ad minima veniam, quis nostrum exercitationem ullam corporis suscipit 
        laboriosam, nisi ut aliquid ex ea commodi consequatur?

    Quis: autem, vel
        eum iure reprehenderit qui in ea voluptate velit esse quam nihil 
        molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas 
        nulla pariatur?
    
    # Related to "de Finibus Bonorum et Malorum"

    At: vero, eos
        et accusamus et iusto odio dignissimos ducimus qui blanditiis
        praesentium voluptatum deleniti atque corrupti quos dolores et quas
        molestias excepturi sint occaecati cupiditate non provident, 

    similique: sunt, in culpa 
        qui officia deserunt mollitia animi, id est laborum et dolorum fuga. 
        Et harum quidem rerum facilis est et expedita distinctio. 
    
    Nam: libero, tempore, 
        cum soluta nobis est eligendi optio cumque nihil impedit quo minus id
        quod maxime placeat facere possimus, omnis voluptas assumenda est, 
        omnis dolor repellendus. 
    
    Temporibus: autem, quibusdam
        et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et 
        voluptates repudiandae sint et molestiae non recusandae. 
    
    Itaque: earum, 
        rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus 
        maiores alias consequatur aut perferendis doloribus asperiores repellat 

    ChangeLog:
    ---------
    45 BC -- Cicero -- Section 1.10.32 of "de Finibus Bonorum et Malorum"
    45 BC -- Cicero -- Section 1.10.31 of "de Finibus Bonorum et Malorum"
    (Did not have Git in 45 BC for commit messages)
    
    """
    
    if echo_time is None:
        # if not given, use the one from the input
        if not myobject.echo_time is None:
            echo_time = myobject.echo_time
        else:
            # no good if you are here, let's see if the data came 
            # from the other route:
            try:
                echo_time = myobject.header['echo_time']
            except KeyError:
                print('Echo time not present')
                AttributeError('echo_time not set')

    if method_to_do_X == 'cauchy-gauss' and correct_cauchy_gauss:
        # don't do anything yet!
        # empirically discovered that cauchy-gauss correction breaks 
        # with more than 5 echoes. 
        echoes_used = {
            'all': slice(0,5), 
            'odd': slice(0,10,2), # since indexing starts from 1
            'even': slice(1,10,2),
        }[which_echo_to_use]
    else:
        echoes_used = {
            'all': slice(None), 
            'odd': slice(None,None,2), # since indexing starts from 1
            'even': slice(1,None,2),
        }[which_echo_to_use]
