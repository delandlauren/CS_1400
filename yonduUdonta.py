'''
Project Name: Yondu Udonta 
Author: Lauren DeLand
Due Date: 02/05/2022
Course: CS1400-005

Description:
Yondu Udonta and his crew of space pirates arrive at the Iron Lotus after several weeks of plundering 
the high seas. Since the crew has been in space for nearly six months, they are ready for a night of 
celebration. Yondu doesn’t want to divvy up the plunder just yet, so he gives each crew member other 
than himself and Peter Quill 3 units and sends them off to the Iron Lotus. 
(We’re keeping the units simple for purposes of the problem, even though 1 unit is about $2.33.)
After the crew has gone, he and Peter count what’s left and decide how to split it up among the crew. 
Yondu takes 13% plunder, which he transfers to a hidden bank account. Yondu gives Peter 11% of the  
remaining units, which Peter transfers to his account. The next morning, the remaining units are 
divided evenly among all of the crew, including Yondu and Quill. Little do they know that Yondu 
and Quill have already taken a cut. If the remaining treasure can’t be split evenly, the units 
left over are given to the Reaver’s Benevolent Fund (RBF).
'''

def main():
    '''
    Program starts here.
    '''
    try:
        reavers = int(input("How many reavers: \n"))
        units = int(input("How many units: \n"))
        pass
    except ValueError:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return

    left_crew = int(reavers - 2)

    #gives us total units spent
    crew_plunder = int(left_crew * 3)

    #gives us leftover units
    plunder_1 = int(units - crew_plunder)

    #gives us Yondus share before crew plunder
    yondu = int(plunder_1 * 0.13 // 1)

    #gives us units after Yondu
    plunder_2 = int(plunder_1 - yondu)

    #gives us peter share before units plundered
    peter = int(plunder_2 * 0.11 // 1)

    #gives us total units after Peter
    plunder_3 = int(plunder_2 - peter)

    #gives us total # of units each crew member gets
    crew_plunder2 = int(plunder_3 // reavers)

    #gives us the total leftover units
    rbf = int(plunder_3 % reavers)

    #gives us Yondu and Peters shares after crew plunder
    yondu = int(yondu + crew_plunder2)
    peter = int(peter + crew_plunder2)

    #print statements
    print("Yondu's share: {}".format(yondu))
    print("Peter's share: {}".format(peter))
    print("Crew: {}".format(crew_plunder2))
    print("RBF: {}".format(rbf))

    pass

if __name__ == "__main__":
    main()
