.. code:: ipython3

    import statistics
    from statistics import mode
    
    
    lis = []
    counter = 0
    word = 0
    rpt = 0
    start = 0
    words =0
    
    
    
    inp = input("write something: ")
    inp = inp.strip()  # remove spaces from start and end of the input
    inp = inp.capitalize() # capitalized the input
    nlis = list(inp.split(" "))   
    words = len(nlis)
    
    rslt = mode(nlis)
    rpt = nlis.count(rslt)
    print("Total words in the text: ", words)
    if rpt>1:
        print ("Your Most repeated word is: '", rslt,"'")
        print ("'", rslt,"'","has occured :", rpt, "times in your text. Try to use its synonyms if the use of word is not absolutely necessary.")
    else:
        print(" All words in your writing are Unique, we have found No any repetations of words in your text.") 


.. parsed-literal::

    write something:         
    

.. parsed-literal::

    Total words in the text:  1
     All words in your writing are Unique, we have found No any repetations of words in your text.
    

