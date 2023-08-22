.. code:: ipython3

    base = input("input base number: ")
    power = input("input power: ")
    
    pow = float(power) 
    bas = float(base)
    result = bas
    count = 0
    
    if pow== 1 :
            print(base,"X 1 = ",(result*pow))
           # result = result * bas
            count = count+1
    else:
            while  count < (pow-1):
                print(result,"X",base,"=",(result*bas))
                result = result * bas
                count = count+1 
    #counter =0
    #while counter <pow :
     #   print(base +"X"+power,"")
     #   counter = counter+1
        
    #print(base * pow)
    #print (result)
        


.. parsed-literal::

    input base number:  1
    input power:  2
    

.. parsed-literal::

    1 X 1 = 1
    

