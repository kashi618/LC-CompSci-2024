
# sin,cos,tan uses radians, we need a converter to radians from degrees

# Does your triangle have a 90 degree angle?

    # Yes, 90 degree triangle
        # Do you want to find a Side or an Angle
            # Sides:
                # How many sides are known to the user?
                    # 2 sides:
                        # Pythagoras:
                            # Input 2 sides, output unknown side
                            # Output unknown side               
                    # 1 side:
                        # Sin (1 Side, 1 Angle):
                            # input known side and angle
                            # output unknown side
                        
                        # Cos (1 Side, 1 Angle):
                            # input known side and angle
                            # output unknown side
                        
                        # Tan (1 Side, 1 Angle):
                            # input known side and angle
                            # output unknown side
            
            # Angles:
                # invSin (2 sides):
                    # input known 2 sides
                    # output unknown angle
                
                # invCos (2 sides):
                    # input known 2 sides
                    # output unknown angle
                
                # invTan (2 sides):
                    # input known 2 sides
                    # output unknown angle
        
        
    # No, non 90 degree triangle
        # Do you want to find a side or an angle?
            # Side:
                # How many sides are known?
                    # 1 side:
                        # ASA 1 side  2 angle           outputs side and angle
                        # sine rule
                    
                    # 2 sides:
                    
                        # SAS 2 sides 1 angle           outputs side and angle
                            # cosine rule
                
            # Angle:
                # How many sides are known?
        
                # 0 sides 2 angles:
                    # AAA
                    # 180 degree angle rule
             
                # 1 side:
                    # ASA 1 side  2 angle               outputs side and angle
                    # sine rule
            
                # 2 sides:
                
                    # SAS 2 sides 1 angle               outputs side and angle
                        # cosine rule
