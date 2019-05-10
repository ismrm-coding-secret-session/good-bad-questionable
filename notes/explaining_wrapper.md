# When running a complicated pipeline

* might evolve like living beings (working but not optimal solutions are not revisited (:thumbsdown:)
* once need to apply to a project, want it to be wrapt and easy to apply :question:
  -> enter! 

## The Almighty Wrapper
  
  ![title-v1](./figs/the_wrapper_title_v1.png) (with ``the_path`` in the argument)

### OK, we give up on the input
* then you apply it to a bit of a different data and it quickly becomes to much of a pain to maintain meaningfull import wrapped, 
  -> so enter!
  
  ![title-v1](./figs/the_wrapper_title_v2.png) 
  
  ...because there has to be something unified for the rest of the pipeline to build on top :question:
  **IMHO:** much like in Hawkings' someone-elses-words each formula halves the number of readers... $E = mc^2$
  Each custom class incorporated in the core of the algorithms reduces the number of people contributing to the code (we all love numpy or reimplementing algos from matlab's scratch). Plus, you pay the penalty of calling API of your custom objects in algorithms.

### If ``myobject``-abstraction [leaks](https://en.wikipedia.org/wiki/Leaky_abstraction)...

![echoes-1](./figs/the_wrapper_echoes-1.png) 

..you want to add a hook!.. :thumbsdown:

(to control corrupted object [the world we live in is cruel, some data come inconsistent]) 

![echoes-2](./figs/the_wrapper_echoes-2.png) 

(But then if you add the hook, it must have priority over the object, so the flow control starts to build up, and in some other dataset ther might be other source of metainformation)
**IMHO:** separate preprocessing run to normalize and unify the data