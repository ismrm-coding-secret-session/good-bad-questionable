def theallmightywrapper(myobject, **kwargs):
	""" Meant to run a very complicated processing pipeline

	<actually meaningfull high level description>

	<expectations about myobject and a bit of its API here>

	Started describing the options:

	recompute_all: bool, optional
		If True, all intermediate results, if found on the disc, will be recomputed
	save_intermediate: bool, optional
		Defines if intermediate results must be saved to the disc
	intermediate_folder : str, optional
		Path to the intermediate results folder. By default os.path.join(os.getcwd(), '_intermediate')
	echo_time : iterable, float, optional
		(necessary for the processing) If given overwrites the echo time from the myobject class
	
	first_used_echo_index : int, default: 0
	last_used_echo_index : int, default: -1
	which_echo_to_use : str, {'even','odd','all'}, optional
		default: 'all'
	
	use_<this-very-special-thing>_index: int, optional
		I happened to work on a dataset which has this feature, so this flag will forever hang around here

	method_to_do_X : str, {'cauchy-gauss', 'iterative_splitting'}, optional
		bla-bla, default: iterative_splitting
	correct_cauchy_gauss: bool, optional
		Since cauchy-gauss is inexact, apply the following workaround...

"""
	if echo_time is None:
		# if not given, use the one from the I/O
		if not myobject.echo_time is None:
			echo_time = myobject.echo_time
		else:
			# no good if you are here, let's see if the data came from the other route:
			try:
				echo_time = myobject.header['echo_time']
			except KeyError:
				print('Echo time not present')
				AttributeError('echoTime not set')

	if method_to_do_X == 'cauchy-gauss':
		# don't do anything yet!
		if correct_cauchy_gauss:
			# empirically discovered that cauchy-gauss correction breaks with more than 5 echoes. As a workaround, let's update first_used_echo_index
			if len(echoes_used) > 5:
				if which_echo_to_use == 'all':
					first_used_echo_index += (len(echoes_used) - 5)
				else:
					first_used_echo_index += (len(echoes_used) - 5) // 2 + 1 
			# do I need to update anything else?