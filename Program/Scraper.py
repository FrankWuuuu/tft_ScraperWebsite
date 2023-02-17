import imp
from pickle import TRUE
from bs4 import BeautifulSoup
import requests 
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import json



print('------------------------------------')
print()
print()

offensiveItems = [
    'Archangel\'s Staff',
    'Bloodthirster',
    'Blue Buff',
    'Deathblade',
    'Edge of Night',
    'Giant Slayer',
    'Guinsoo\'s Rageblade',
    'Hand of Justice',
    'Hextech Gunblade',
    'Infinity Edge',
    'Jeweled Gauntlet',
    'Last Whisper',
    'Morellonomicon',
    'Quicksilver',
    'Rabadon\'s Deathcap',
    'Rapid Firecannon',
    'Runaan\'s Hurricane',
    'Spear of Shojin',
    'Statikk Shiv',
    'Titan\'s Resolve',
    'Titan’s Resolve',
    'Quicksilver',
    'Ionic Spark'
    
]
#----------------------------------TFTACTICS.GG----------------------------------#

def tftactics ():
    tftacticsDataBase= []

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get('https://tftactics.gg/tierlist/team-comps')

    def cycleUnitsPrint (anyCostUnits):
        for unit in anyCostUnits:
            
            champName = unit.find_element(By.CLASS_NAME, "team-character-name")
            print(champName.text, end = ' ')
            
            try:
                itemsGroup = unit.find_element(By.CLASS_NAME, "character-items")
                items = itemsGroup.find_elements(By.CLASS_NAME, "character-icon")
                print("{", end = "")
                i = 0
                for item in items:
                    
                    
                    print(item.get_attribute("alt"), end = "")
                    if (i != len(items)-1):
                        print(", ", end = "")
                        i= i+ 1
                    
                
                print("} ", end = "")
            except:
                pass

    def cycleUnits (anyCostUnits):
        for unit in anyCostUnits:
            champName = unit.find_element(By.CLASS_NAME, "team-character-name").text

            if unit.get_attribute("class").endswith('l3'):
                threeStar.append(champName)
            
            
            try:
                itemsGroup = unit.find_element(By.CLASS_NAME, "character-items")
                items = itemsGroup.find_elements(By.CLASS_NAME, "character-icon")
                arrItems = []

                carryItemCount = 0
                for item in items:
                    itemName = item.get_attribute("alt")
                    arrItems.append(itemName)
                    
                    for offensiveItem in offensiveItems:
                        if itemName == offensiveItem:
                            carryItemCount = carryItemCount+ 1
                    # print (carryItemCount)
                if carryItemCount>1:
                    carry.append(champName)

                
                arrUnits[champName] = arrItems
                    
                
            except:
                arrUnits[champName] = []
            
    
    tierlist = driver.find_elements(By.CLASS_NAME, "tier-group" )
    
    for tier in tierlist:                                                               #tier
        arrTier = []
        teamComps = tier.find_elements(By.CLASS_NAME, "team-characters" ) 
        # print("TIER ----------------")
        
        for team in teamComps:                                                      #teamcomp
            arrTeamComp = {}
            carry = []
            threeStar = []
            arrUnits = {}
            # arrItemsForComp = []
            # print()
            # print()
            # print("     ", end = '')
            oneCostUnits = team.find_elements(By.CLASS_NAME, "characters-item.c1") 
            twoCostUnits = team.find_elements(By.CLASS_NAME, "characters-item.c2") 
            threeCostUnits = team.find_elements(By.CLASS_NAME, "characters-item.c3") 
            sixCostUnits = team.find_elements(By.CLASS_NAME, "characters-item.c6") 
            fourCostUnits = team.find_elements(By.CLASS_NAME, "characters-item.c4") 
            sevenCostUnits = team.find_elements(By.CLASS_NAME, "characters-item.c7") 
            fiveCostUnits = team.find_elements(By.CLASS_NAME, "characters-item.c5") 
            eightCostUnits = team.find_elements(By.CLASS_NAME, "characters-item.c8")  
            cycleUnits(oneCostUnits)
            cycleUnits(twoCostUnits)
            cycleUnits(threeCostUnits)
            cycleUnits(sixCostUnits)
            cycleUnits(fourCostUnits)
            cycleUnits(sevenCostUnits)
            cycleUnits(fiveCostUnits)
            cycleUnits(eightCostUnits)
            # cycleUnitsPrint(oneCostUnits)
            # cycleUnitsPrint(twoCostUnits)
            # cycleUnitsPrint(threeCostUnits)
            # cycleUnitsPrint(fourCostUnits)
            # cycleUnitsPrint(eightCostUnits)
            # cycleUnitsPrint(fiveCostUnits)
            # cycleUnitsPrint(tenCostUnits)

        
            # print()
            # print() 

            arrTeamComp['carry']= carry
            arrTeamComp['units']= arrUnits
            # arrTeamComp['threeStars']= threeStar
            # arrTeamComp['items']= arrItemsForComp
            arrTier.append(arrTeamComp)
            # print(arrTeamComp)
        tftacticsDataBase.append(arrTier)

    json_object = json.dumps(tftacticsDataBase, indent=4)
    with open("tftactics.json", "w") as outfile:
        outfile.write(json_object)
    driver.close()
    return tftacticsDataBase






    
    print()
    print()
    print('------------------------------------')

#----------------------------------LOLCHESS----------------------------------#

def lolchess ():
    lolChessDataBase= []

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get('https://lolchess.gg/meta')

   
    # tierlist = driver.find_elements(By.CLASS_NAME, "guide-meta__group__content" )
    driver.find_element(By.XPATH, "//*[@id=\"toggle-meta-show-name\"]/img[2]" ).click()

    teamComps = driver.find_elements(By.CLASS_NAME, "guide-meta__deck-box" ) 
    for team in teamComps:
        arrTeamComp = {}
        carry = []
        arrItemsOfComp = []
        arrUnits = {}

        anyCostUnits = team.find_elements(By.CLASS_NAME, "tft-champion-box") 
        
        for unit in anyCostUnits:
            champName = unit.find_element(By.CLASS_NAME, "name").text 

            itemContainer = unit.find_element(By.CLASS_NAME, "tft-items") 
            itemList = itemContainer.find_elements(By.TAG_NAME, "img")
            carryItemCount = 0
            if len(itemList) != 0:
                arrItems = []
                for item in itemList:
                    itemName = item.get_attribute("alt")
                    arrItems.append(itemName)

                    for offensiveItem in offensiveItems:
                        if offensiveItem == itemName:
                            carryItemCount = carryItemCount+ 1
                if carryItemCount>1:
                        carry.append(champName)

                arrUnits[champName] = arrItems
            else:
                arrUnits[champName] = []


        arrTeamComp['carry']= carry
        arrTeamComp['units']= arrUnits
        # arrTeamComp['items']= arrItemsOfComp
        lolChessDataBase.append(arrTeamComp)
    # print(lolChessDataBase)
    json_object = json.dumps(lolChessDataBase, indent=4)
    with open("lolchess.json", "w") as outfile:
        outfile.write(json_object)
    driver.close()
    return lolChessDataBase
    
#----------------------------------Bunnymuffins----------------------------------#
def bunnymuffins ():
    bunnymuffinsDatabase= []

    def cycleUnits (anyCostUnits):
        for unit in anyCostUnits:
            champName = unit.find_element(By.CLASS_NAME, "name").text
            
            
            
            itemsGroup = unit.find_element(By.CLASS_NAME, "items")
            items = itemsGroup.find_elements(By.TAG_NAME, "img")
            arrItems = []

            carryItemCount = 0
            if len(items) !=0:
                for item in items:
                    itemName = item.get_attribute("alt")    
                    arrItems.append(itemName)
                    
                    for offensiveItem in offensiveItems:
                        if itemName == offensiveItem:
                            carryItemCount = carryItemCount+ 1
                    # print (carryItemCount)
                if carryItemCount>1:
                    carry.append(champName)
                
                
                arrUnits[champName] = arrItems
                
                
            else:
                arrUnits[champName] = []
            # print('cuum')

    
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    
    driver.get('https://bunnymuffins.lol/meta/')

    teamcompsLinkFinder = driver.find_elements(By.CLASS_NAME, "gb-container")
    
    teamcomps = []
    isNewTier = True
    tier = -1

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    

    for teamcomp in teamcompsLinkFinder:
        
        linkcontainerWpBlockImageSizeLarge = teamcomp.find_elements(By.CLASS_NAME, "wp-block-image.size-large")
        
        if len(linkcontainerWpBlockImageSizeLarge) == 0:
            if isNewTier:
                tier += 1
                isNewTier = False
                teamcomps.append([])

        else:
            if not isNewTier:
                isNewTier = True
            for thing in linkcontainerWpBlockImageSizeLarge:
                try:
                    linkContainer = thing.find_element(By.TAG_NAME, "a")
                    teamcomps[tier].append(linkContainer.get_attribute("href"))
                except:
                    pass
    
    for teamcomp in teamcomps:
        if teamcomp == []:
            teamcomps.remove(teamcomp)

  


    for tier in teamcomps:
        arrTier = []
        for teamcomp in tier:
            arrTeamComp = {}
            carry = []                                          
            arrUnits = {}
            driver.get(teamcomp)
            
            
            oneCostUnits = driver.find_elements(By.CLASS_NAME, 'champion-slot.cost-1')
            twoCostUnits = driver.find_elements(By.CLASS_NAME, 'champion-slot.cost-2')
            threeCostUnits = driver.find_elements(By.CLASS_NAME, 'champion-slot.cost-3')
            sixCostUnits = driver.find_elements(By.CLASS_NAME, 'champion-slot.cost-6')
            fourCostUnits = driver.find_elements(By.CLASS_NAME, 'champion-slot.cost-4')
            sevenCostUnits = driver.find_elements(By.CLASS_NAME, 'champion-slot.cost-7')
            fiveCostUnits = driver.find_elements(By.CLASS_NAME, 'champion-slot.cost-5')
            eightCostUnits = driver.find_elements(By.CLASS_NAME, 'champion-slot.cost-8')
            cycleUnits(oneCostUnits)
            cycleUnits(twoCostUnits)
            cycleUnits(threeCostUnits)
            cycleUnits(sixCostUnits)
            cycleUnits(fourCostUnits)
            cycleUnits(sevenCostUnits)
            cycleUnits(fiveCostUnits)
            cycleUnits(eightCostUnits)

            arrTeamComp['carry']= carry
            arrTeamComp['units']= arrUnits
            arrTier.append(arrTeamComp)
            
            # print(arrTeamComp)
        bunnymuffinsDatabase.append(arrTier)
    # print(bunnymuffinsDatabase)
    
    json_object = json.dumps(bunnymuffinsDatabase, indent=4)
    with open("bunnymuffins.json", "w") as outfile:
        outfile.write(json_object)

    driver.close()
    return bunnymuffinsDatabase
    
        


    
    


#----------------------------------//----------------------------------#


print(tftactics())
print(lolchess())
# print(bunnymuffins())

# oneCostUnits = driver2.find_elements(By.CLASS_NAME, "champion-slot drop mr-1 champion-slot--27 cost-1")
# for onecost in oneCostUnits:

#     unitName = onecost.find_element(By.CLASS_NAME, "name").text
#     print(unitName)


print()
print()
print('------------------------------------')