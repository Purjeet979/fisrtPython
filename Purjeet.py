li1 = ["Sun Temple (1984)","Agra Fort (1983)",
"Ajanta Caves (1983)","Elephanta Caves (1987)",
"Ellora Caves (1983)","Taj Mahal (1983)","The Jantar Mantar(2010)","Western Ghats (2012)"]
for attempt in range (1,13):
            print ("\nAttempt number:", attempt)
            print("\n             UNESCO - WORLD HERITAGE SITES:-")
            print("..........................................................")
            print("\nThe list has the following elements-")
            for i in range(len(li1)):  
                    print( li1[i])       
            print("\n 1. Information about Agra Fort (1983) ")
            print(" 2. Information about Sun Temple (1984)")
            print(" 3. Information about Ajanta Caves (1983)")
            print(" 4. Information about Elephanta Caves (1987) ")
            print(" 5. Information about Ellora Caves (1983) ")
            print(" 6. Information about Taj Mahal (1983)")
            print(" 7. Information about The Jantar Mantar(2010)")
            print(" 8. Information about Western Ghats (2012)")
            print(" 9. Sort the list in ascending order")
            print(" 10. Sort the list in descending order")
            print(" 11. Delete an existing element by its position")
            print(" 12. Delete an existing element by its value")
            print(" 13. Modify an existing element")
            print("..........................................................")
            choice = int(input("\nENTER YOUR CHOICE (1-13): "))
            if choice == 1: 
                      print("\nAgra Fort (1983) ")
                      print("................")
                      print("Near the gardens of the Taj Mahal stands the important 16th-century Mughal monument known as the Red Fort of Agra. This powerful fortress of red sandstone encompasses, within its 2.5-km-long enclosure walls, the imperial city of the Mughal rulers. It comprises many fairy-tale palaces, such as the Jahangir Palace and the Khas Mahal, built by Shah Jahan; audience halls, such as the Diwan-i-Khas; and two very beautiful mosques.")
           
            elif choice == 2:
                      print("\nSun Temple (1984)")
                      print(".................")
                      print("On the shores of the Bay of Bengal, bathed in the rays of the rising sun, the temple at Konarak is a monumental representation of the sun god Surya's chariot; its 24 wheels are decorated with symbolic designs and it is led by a team of six horses. Built in the 13th century, it is one of India's most famous Brahman sanctuaries.")            
           
            elif choice == 3:
                      print("\nAjanta Caves (1983)")
                      print("...................")
                      print("The first Buddhist cave monuments at Ajanta date from the 2nd and 1st centuries B.C. During the Gupta period (5th and 6th centuries A.D.), many more richly decorated caves were added to the original group. The paintings and sculptures of Ajanta, considered masterpieces of Buddhist religious art, have had a considerable artistic influence.")
           
            elif choice == 4:
                      print("\nElephanta Caves (1987)")
                      print("......................")
                      print("The 'City of Caves', on an island in the Sea of Oman close to Bombay, contains a collection of rock art linked to the cult of Shiva. Here, Indian art has found one of its most perfect expressions, particularly the huge high reliefs in the main cave.")
           
            elif choice == 5:
                      print("\nEllora Caves (1983)")
                      print("......................")
                      print("These 34 monasteries and temples, extending over more than 2 km, were dug side by side in the wall of a high basalt cliff, not far from Aurangabad, in Maharashtra. Ellora, with its uninterrupted sequence of monuments dating from A.D. 600 to 1000, brings the civilization of ancient India to life. Not only is the Ellora complex a unique artistic creation and a technological exploit but, with its sanctuaries devoted to Buddhism, Hinduism and Jainism, it illustrates the spirit of tolerance that was characteristic of ancient India.") 
            
            elif choice == 6:
                      print("\nTaj Mahal (1983)")
                      print("................")
                      print("An immense mausoleum of white marble, built in Agra between 1631 and 1648 by order of the Mughal emperor Shah Jahan in memory of his favourite wife, the Taj Mahal is the jewel of Muslim art in India and one of the universally admired masterpieces of the world's heritage.")         
           
            elif choice == 7:
                      print("\nThe Jantar Mantar(2010)")
                      print(".......................")
                      print("The Jantar Mantar, in Jaipur, is an astronomical observation site built in the early 18th century. It includes a set of some 20 main fixed instruments. They are monumental examples in masonry of known instruments but which in many cases have specific characteristics of their own. Designed for the observation of astronomical positions with the naked eye, they embody several architectural and instrumental innovations. This is the most significant, most comprehensive, and the best preserved of India's historic observatories. It is an expression of the astronomical skills and cosmological concepts of the court of a scholarly prince at the end of the Mughal period.")         
           
            elif choice == 8:
                      print("\nWestern Ghats (2012)")
                      print("....................")
                      print("Older than the Himalaya mountains, the mountain chain of the Western Ghats represents geomorphic features of immense importance with unique biophysical and ecological processes. The site’s high montane forest ecosystems influence the Indian monsoon weather pattern. Moderating the tropical climate of the region, the site presents one of the best examples of the monsoon system on the planet. It also has an exceptionally high level of biological diversity and endemism and is recognized as one of the world’s eight ‘hottest hotspots’ of biological diversity. The forests of the site include some of the best representatives of non-equatorial tropical evergreen forests anywhere and are home to at least 325 globally threatened flora, fauna, bird, amphibian, reptile and fish species.")
            
            elif choice == 9:
                      li1.sort()
                      print("\nThe list has been sorted",li1)  
            
            elif choice == 10:
                      li1.sort(reverse = True)
                      print("\nThe list has been sorted in reverse order",li1)        
           
            elif choice == 11:
                       i = int(input("Enter the position of the element to be deleted: "))
                       if i < len(li1):
                            element = li1.pop(i)
                            print("The element",element,"has been deleted\n")
                       else:
                           print("\nPosition of the element is more then the length of list")
           
            elif choice == 12:
                      element = int(input("\nEnter the element to be deleted: "))
                      if element in li1:
                               li1.remove(element)
                               print("\nThe element",element,"has been deleted\n",li1)
                      else:
                          print("\nElement",element,"is not present in the list")              
           
            elif choice == 13:
                       i = int(input("Enter the position of the element to be modified: "))                      
                       if i < len(li1):
                              newelement = eval(input("Enter the new element: "))
                              oldelement = li1[i]
                              li1[i] = newelement
                              print("The element",oldelement,"has been modified\n",li1)
                       else:
                               print("Position of the element is more then the length of list")   
          