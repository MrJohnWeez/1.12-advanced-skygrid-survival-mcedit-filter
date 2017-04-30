# 1.12 Advanced Custom Skygrid mcedit filter by MrJohnWeez
# YouTube, Github, Twitter: @MrJohnWeez

#Feel free to use my filter but please give me credit @MrJohnWeez ~Thanks

# I was able to gain knowlege from these great people:
# Special thanks to Sethbling for custom distributions help and biome modification code
# Special thanks to StealthyExpert for 1.11 chest item modification guidance
# Special thanks to Zylion for some logic help on mega blocks

#######################################################################################################################################


#Imports all libraries needed:
import math
from numpy import zeros
import random
from pymclevel import TAG_List, TAG_Byte, TAG_Int, TAG_Compound, TAG_Short, TAG_Float, TAG_Double, TAG_String, TAG_Long
from pymclevel import MCSchematic, TileEntity
from random import randint
import datetime


displayName = "Advanced SkyGrid (1.12+) By_MrJohnWeez"

#McEdit imput language
inputs = (
	("Random blocks", True),
	("Block (if not random)", "blocktype"),
	("Scale of block chunks", (1, 1, 128)),
	("Block spacing Horizontal", (3, 0, 100)),
	("Block spacing Vertical", (3, 0, 100)),
	("Create End Portal", True),
	("Create Spawn Platform", True),
	("Stats for nerds", True),
	("Safe Mode", True),
	("Enable spawners", True),
	("Enable chests", True),
	("Spawner probability (Lower = rare):", (180, 0, 10000000)),
	("Chest probability (Lower = rare):", (170, 0, 10000000)),
	("Each island consists of one block type", True),
	("Fill with air blocks", False),
	("World Type", ("Overworld","Nether","End","Normal","Ice","Jungle","Swamp","Desert","Ocean","Mushroom","Mesa","OVERLOADED!")),
	("Set biome with world type", True),
	("Biome (if not with world type)",  
				("Current Biome",
				"Ocean",
                "Plains",
                "Desert",
                "Extreme Hills",
                "Forest",
                "Taiga",
                "Swamppland",
                "River",
                "Hell (Nether)",
                "The End",
                "Frozen Ocean",
                "Frozen River",
                "Ice Plains",
                "Ice Mountains",
                "Mushroom Island",
                "Mushroom Island Shore",
                "Beach",
                "Desert Hills",
                "Forest Hills",
                "Taiga Hills",
                "Extreme Hills Edge",
                "Jungle",
                "Jungle Hills",
                "Jungle Edge",
                "Deep Ocean",
                "Stone Beach",
                "Cold Beach",
                "Birch Forest",
                "Birch Forest Hills",
                "Roofed Forest",
                "Cold Taiga",
                "Cold Taiga Hills",
                "Mega Taiga",
                "Mega Taiga Hills",
                "Extreme Hills+",
                "Savanna",
                "Savanna Plateau",
                "Mesa",
                "Mesa Plateau F",
                "Mesa Plateau",
                "The Void",
                "Sunflower Plains",
                "Desert M",
                "Extreme Hills M",
                "Flower Forest",
                "Taiga M",
                "Swampland M",
                "Ice Plains Spikes",
                "Ice Mountains Spikes",
                "Jungle M",
                "JungleEdge M",
                "Birch Forest M",
                "Birch Forest Hills M",
                "Roofed Forest M",
                "Cold Taiga M",
                "Mega Spruce Taiga",
                "Mega Spruce Taiga Hills",
                "Extreme Hills+ M",
                "Savanna M",
                "Savanna Plateau M",
                "Mesa (Bryce)",
                "Mesa Plateau F M",
                "Mesa Plateau M",
                "(Uncalculated)",
    )),
	("Game version", ("1.12+","1.11","Older")),
	)
	
#Define all biomes with their minecraft value
biomes = {
    "Ocean": 0,
    "Plains": 1,
    "Desert": 2,
    "Extreme Hills": 3,
    "Forest": 4,
    "Taiga": 5,
    "Swamppland": 6,
    "River": 7,
    "Hell (Nether)": 8,
    "The End": 9,
    "Frozen Ocean": 10,
    "Frozen River": 11,
    "Ice Plains": 12,
    "Ice Mountains": 13,
    "Mushroom Island": 14,
    "Mushroom Island Shore": 15,
    "Beach": 16,
    "Desert Hills": 17,
    "Forest Hills": 18,
    "Taiga Hills": 19,
    "Extreme Hills Edge": 20,
    "Jungle": 21,
    "Jungle Hills": 22,
    "Jungle Edge": 23,
    "Deep Ocean": 24,
    "Stone Beach": 25,
    "Cold Beach": 26,
    "Birch Forest": 27,
    "Birch Forest Hills": 28,
    "Roofed Forest": 29,
    "Cold Taiga": 30,
    "Cold Taiga Hills": 31,
    "Mega Taiga": 32,
    "Mega Taiga Hills": 33,
    "Extreme Hills+": 34,
    "Savanna": 35,
    "Savanna Plateau": 36,
    "Mesa": 37,
    "Mesa Plateau F": 38,
    "Mesa Plateau": 39,
    "The Void": 127,
    "Sunflower Plains": 129,
    "Desert M": 130,
    "Extreme Hills M": 131,
    "Flower Forest": 132,
    "Taiga M": 133,
    "Swampland M": 134,
    "Ice Plains Spikes": 140,
    "Ice Mountains Spikes": 141,
    "Jungle M": 149,
    "JungleEdge M": 151,
    "Birch Forest M": 155,
    "Birch Forest Hills M": 156,
    "Roofed Forest M": 157,
    "Cold Taiga M": 158,
    "Mega Spruce Taiga": 160,
    "Mega Spruce Taiga Hills": 161,
    "Extreme Hills+ M": 162,
    "Savanna M": 163,
    "Savanna Plateau M": 164,
    "Mesa (Bryce)": 165,
    "Mesa Plateau F M": 166,
    "Mesa Plateau M": 167,
    "(Uncalculated)": -1,
}
	
#Function creates a chest with "Random" Items inside
def createChestBlockData(x, y, z, options):
	worldtype = options["World Type"]
	total = 0
	cump = {}
	
	if worldtype == "Overworld":
		pitems = overworldChestLoot(options)
	elif worldtype == "Nether":
		pitems = netherChestLoot(options)
	elif worldtype == "End":
		pitems = endChestLoot(options)
	elif worldtype == "Normal":
		pitems = normalChestLoot(options)
	elif worldtype == "Ice":
		pitems = iceChestLoot(options)
	elif worldtype == "Jungle":
		pitems = jungleChestLoot(options)
	elif worldtype == "Swamp":
		pitems = swampChestLoot(options)
	elif worldtype == "Desert":
		pitems = desertChestLoot(options)
	elif worldtype == "Ocean":
		pitems = oceanChestLoot(options)
	elif worldtype == "Mushroom":
		pitems = mushroomChestLoot(options)
	elif worldtype == "Mesa":
		pitems = mesaChestLoot(options)
	elif worldtype == "OVERLOADED!":
		pitems = overloadedChestLoot(options)
	
	#Unnormilized distribution calculation
	for key, value in pitems.iteritems():
		cump[key] = (total, total + value)
		total += value
	
	chest = TAG_Compound()
	chest["y"] = TAG_Int(y)
	
	if options["Game version"] == "Older":
		chest["id"] = TAG_String("Chest")
	else:
		chest["id"] = TAG_String("chest")
	chest["x"] = TAG_Int(x)
	chest["z"] = TAG_Int(z)
	items = TAG_List()
	
	#Generates a "random" item, for all 27 slots, to put into the chest
	for c in xrange(0, 27):
		minecraftchest = TAG_Compound()
		itemName,data,amount = pickItem(cump, total)
		minecraftchest["id"] = TAG_String(itemName)
		minecraftchest["Damage"] = TAG_Short(data)
		minecraftchest["Count"] = TAG_Byte(amount)
		tag = TAG_Compound()
		minecraftchest["tag"] = tag
		minecraftchest["Slot"] = TAG_Byte(c)
		items.append(minecraftchest)
		
	chest["Items"] = items
	return chest
	
def statsForNerds(level, box, options):
	Stats = options["Stats for nerds"]
	print "Running...SkyGrid MCEdit Filter"
	dx = box.maxx-box.minx
	dy = box.maxy-box.miny
	dz = box.maxz-box.minz
	total = dx*dy*dz
	print "Selected Blocks: %d" % (total)
	if total >= 3000000 and options["Safe Mode"]:
		return False
	else:
		if Stats:
			timeS = (4000*math.exp(8*(10**-7)*total*2))/1000
			timeM = 4000*math.exp(8*(10**-7)*total*2)
			if total >= 4000000:
				print "----!!!!---------WARNING---------!!!!----"
				print "Too many blocks selected. Program may crash!"
				print "Max estimated run time: 5 Minutes or more"
			elif total >= 3000000:
				print "------------------WARNING------------------"
				print "Program is more efficient under 3 million blocks. Program may crash!"
				print "Max estimated run time: 4 Minutes or more"
			elif total >= 2000000:
				print "------------------WARNING------------------"
				print "Program is more efficient under 2 million blocks. Program may crash!"
				print "Max estimated run time: 3 Minutes or more"
			else:
				print "Max estimated run time: %d Second(s) or %d Milliseconds" % (timeS,timeM)
		return True
	
def perform(level, box, options):
	isSafe = statsForNerds(level, box, options)
	a = datetime.datetime.now()
	#Runs main code
	if isSafe:
		biomeEditor(level, box, options)
		blockPlacer(level, box, options)
		
		#tells McEdit there were changes
		level.markDirtyBox(box)
		
		b = datetime.datetime.now()
		delta = b - a
		print "Time in milliseconds: %d" % (int(delta.total_seconds()* 1000))
	else:
		print "Program has been terminated due to safe mode. Too many blocks were selected."
	print "////////MCEdit Filter By MrJohnWeez////////"
	
	
def biomeEditor(level, box, options):
	worldtype = options["World Type"]
	worldBiome = options["Set biome with world type"]
	
	if worldBiome:
		if worldtype == "Overworld":
			useBiome = "Forest"
		elif worldtype == "Nether":
			useBiome = "Hell (Nether)"
		elif worldtype == "End":
			useBiome = "The End"
		elif worldtype == "Normal":
			useBiome = "Forest"
		elif worldtype == "Ice":
			useBiome = "Ice Plains Spikes"
		elif worldtype == "Jungle":
			useBiome = "Jungle"
		elif worldtype == "Swamp":
			useBiome = "Swamppland"
		elif worldtype == "Desert":
			useBiome = "Savanna"
		elif worldtype == "Ocean":
			useBiome = "Deep Ocean"
		elif worldtype == "Mushroom":
			useBiome = "Mushroom Island"
		elif worldtype == "Mesa":
			useBiome = "Mesa"
		elif worldtype == "OVERLOADED!":
			useBiome = "Forest"
	else:
		useBiome = options["Biome (if not with world type)"]
	
	#Clean biome of tileEntities
	chunkMinx = int(box.minx / 16) * 16
	chunkMinz = int(box.minz / 16) * 16
	
	for x in xrange(chunkMinx, box.maxx, 16):
		for z in xrange(chunkMinz, box.maxz, 16):
			chunk = level.getChunk(x/16, z/16)
			chunk.removeTileEntitiesInBox(box)
			
	if useBiome != "Current Biome":
		print "Running...Biome Changed"
#Code from sethbling: Download https://goo.gl/Ae3IFy
		biome = dict([(trn._(a), b) for a, b in biomes.items()])[useBiome]
		
		for x in xrange(chunkMinx, box.maxx, 16):
			for z in xrange(chunkMinz, box.maxz, 16):
				chunk = level.getChunk(x / 16, z / 16)
				chunk.dirty = True
				array = chunk.root_tag["Level"]["Biomes"].value

				chunkx = int(x / 16) * 16
				chunkz = int(z / 16) * 16

				for bx in xrange(max(box.minx, chunkx), min(box.maxx, chunkx + 16)):
					for bz in xrange(max(box.minz, chunkz), min(box.maxz, chunkz + 16)):
						idx = 16 * (bz - chunkz) + (bx - chunkx)
						array[idx] = biome

				chunk.root_tag["Level"]["Biomes"].value = array
#End of Sethbling's code			
		
	
	
def blockPlacer(level, box, options):
	#Options config
	worldtype = options["World Type"]
	isRandom = options["Random blocks"]
	block = options["Block (if not random)"].ID
	data = options["Block (if not random)"].blockData
	sizescale = options["Scale of block chunks"]
	spaceH = options["Block spacing Horizontal"]
	spaceV = options["Block spacing Vertical"]
	spawners = options["Enable spawners"]
	chests = options["Enable chests"]
	spawnchanceSpawner = options["Spawner probability (Lower = rare):"]
	spawnchanceChest = options["Chest probability (Lower = rare):"]
	fillAir = options["Fill with air blocks"]
	oneblock = options["Each island consists of one block type"]
	portal = options["Create End Portal"]
	worldBiome = options["Set biome with world type"]
	userBiome = options["Biome (if not with world type)"]

	#Define vars
	total = 0
	cump = {}
	
	if worldtype == "Overworld":
		p = overworldp(options)
	elif worldtype == "Nether":
		p = netherp(options)
	elif worldtype == "End":
		p = endp(options)
	elif worldtype == "Normal":
		p = normalp(options)
	elif worldtype == "Ice":
		p = icep(options)
	elif worldtype == "Jungle":
		p = junglep(options)
	elif worldtype == "Swamp":
		p = swampp(options)
	elif worldtype == "Desert":
		p = desertp(options)
	elif worldtype == "Ocean":
		p = oceanp(options)
	elif worldtype == "Mushroom":
		p = mushroomp(options)
	elif worldtype == "Mesa":
		p = mesap(options)
	elif worldtype == "OVERLOADED!":
		p = overloadedp(options)
		
	#Unnormilized distribution calculation
	for key, value in p.iteritems():
		cump[key] = (total, total + value)
		total += value
		
	#only runs if user wants to clear all blocks before running main
	if(fillAir):
		for x in xrange(box.minx, box.maxx):
			for y in xrange(box.miny, box.maxy):
				for z in xrange(box.minz, box.maxz):
					setBlock(level, (0,0), x, y, z)
				
	#MAIN CODE
	print "Running...SkyGrid Generation"
	for x in xrange(box.minx, box.maxx):
		for y in xrange(box.miny, box.maxy):
			for z in xrange(box.minz, box.maxz):
				#Sets "random" block to the lower x y z corner of a cube
				if (((z - 1) % (sizescale + spaceH)) + 1 == 1) and (((y - 1) % (sizescale + spaceV)) + 1 == 1) and \
				(((x - 1) % (sizescale + spaceH)) + 1 == 1):
					if isRandom:
						blockid,dataid = pickblock(cump, total)
						setBlock(level, (blockid,dataid), x, y, z)
						detectBlockId(level, options, blockid, x, y, z)
					else:
						setBlock(level, (block,data), x, y, z)
				
				# Make giant blocks from "Random" blocks in a cube shape
				# Or makes a giant block based on the corner block
				if oneblock:
					if level.blockAt(x, y, z-1) != 0 and (((z-1) % (sizescale+spaceH))+1 >= 2 and ((z-1) % (sizescale+spaceH))+1 <= sizescale):
						pBlockId = level.blockAt(x, y, z-1)
						pDataId = level.blockDataAt(x, y, z-1)
						setBlock(level, (pBlockId,pDataId), x, y, z)
						detectBlockId(level, options, pBlockId, x, y, z)
					elif level.blockAt(x, y-1, z) != 0 and (((y-1) % (sizescale+spaceV))+1 >= 2 and ((y-1) % (sizescale+spaceV))+1 <= sizescale):
						pBlockId = level.blockAt(x, y-1, z)
						pDataId = level.blockDataAt(x, y-1, z)
						setBlock(level, (pBlockId,pDataId), x, y, z)
						detectBlockId(level, options, pBlockId, x, y, z)
					elif level.blockAt(x-1, y, z) != 0 and (((x-1) % (sizescale+spaceH))+1 >= 2 and ((x-1) % (sizescale+spaceH))+1 <= sizescale):
						pBlockId = level.blockAt(x-1, y, z)
						pDataId = level.blockDataAt(x-1, y, z)
						setBlock(level, (pBlockId,pDataId), x, y, z)
						detectBlockId(level, options, pBlockId, x, y, z)
				else: 
					if level.blockAt(x, y, z-1) != 0 and (((z-1) % (sizescale+spaceH))+1 >= 2 and ((z-1) % (sizescale+spaceH))+1 <= sizescale):
						blockid,dataid = pickblock(cump, total)
						setBlock(level, (blockid,dataid), x, y, z)
						detectBlockId(level, options, blockid, x, y, z)
					elif level.blockAt(x, y-1, z) != 0 and (((y-1) % (sizescale+spaceV))+1 >= 2 and ((y-1) % (sizescale+spaceV))+1 <= sizescale):
						blockid,dataid = pickblock(cump, total)
						setBlock(level, (blockid,dataid), x, y, z)
						detectBlockId(level, options, blockid, x, y, z)
					elif level.blockAt(x-1, y, z) != 0 and (((x-1) % (sizescale+spaceH))+1 >= 2 and ((x-1) % (sizescale+spaceH))+1 <= sizescale):
						blockid,dataid = pickblock(cump, total)
						setBlock(level, (blockid,dataid), x, y, z)
						detectBlockId(level, options, blockid, x, y, z)

	#generating end portal
	if portal:
		if (worldtype == "Overworld" or worldtype == "Normal"):
			#Finds middles
			dx = box.maxx - box.minx
			dz = box.maxz - box.minz
			middlex = box.minx + int(dx / 2)
			middlez = box.minz + int(dz / 2)
			y = box.miny + spaceV
			if y <= box.maxy and middlex+4 <= box.maxx and middlez+4 <= box.maxz:
				# set portal blocks and air
				for xunit in xrange(1,4):
					setBlock(level, (120,0), middlex+xunit, y, middlez)
				for zunit in xrange(1,4):
					for xunit in xrange(1,4):
						setBlock(level, (0,0), middlex+xunit, y, middlez+zunit)
				for zunit in xrange(1,4):
					setBlock(level, (120,3), middlex, y, middlez+zunit)
				for xunit in xrange(1,4):
					setBlock(level, (120,2), middlex+xunit, y, middlez+4)
				for zunit in xrange(1,4):
					setBlock(level, (120,1), middlex+4, y, middlez+zunit)
					
	#Makes spawn platform in the middle of selection
	if options["Create Spawn Platform"]:
		dx = box.maxx - box.minx
		dz = box.maxz - box.minz
		middlex = box.minx + int(dx / 2)
		middlez = box.minz + int(dz / 2)
		for zunit in xrange(-6,6):
			for xunit in xrange(-6,6):
				setBlock(level, (95,3), middlex+xunit, box.maxy-1, middlez+zunit)
		
	
#Makes titleEnitity data for Spanwer/Chest
def detectBlockId(level, options, pBlockId, x, y, z):
	worldtype = options["World Type"]
	chunk = level.getChunk(x/16, z/16)
	if(pBlockId == 54):
		chunk.TileEntities.append( createChestBlockData(x, y, z, options))
	elif(pBlockId == 52):
		chunk.TileEntities.append( setSpawnerAt(level, options, worldtype, x, y, z))
		
		
#Creates a "Random" Spanwer via world option
def setSpawnerAt(level, options, worldtype, x, y, z):
	worldtype = options["World Type"]
	total = 0
	cump = {}
	
	if worldtype == "Overworld":
		pspawn = overworldSpawns()
	elif worldtype == "Nether":
		pspawn = netherSpawns()
	elif worldtype == "End":
		pspawn = endSpawns()
	elif worldtype == "Normal":
		pspawn = normalSpawns()
	elif worldtype == "Ice":
		pspawn = iceSpawns()
	elif worldtype == "Jungle":
		pspawn = jungleSpawns()
	elif worldtype == "Swamp":
		pspawn = swampSpawns()
	elif worldtype == "Desert":
		pspawn = desertSpawns()
	elif worldtype == "Ocean":
		pspawn = oceanSpawns()
	elif worldtype == "Mushroom":
		pspawn = mushroomSpawns()
	elif worldtype == "Mesa":
		pspawn = mesaSpawns()
	elif worldtype == "OVERLOADED!":
		pspawn = overloadedSpawns()
		
	#Unnormilized distribution calculation
	for key, value in pspawn.iteritems():
		cump[key] = (total, total + value)
		total += value

	#Spawner Properties
	spawnName = pickSpawn(cump, total)
	spawner = TileEntity.Create("minecraft:mob_spawner")
	TileEntity.setpos(spawner, (x, y, z))
	spawner["SpawnData"] = TAG_Compound() #spawnData acts like a folder
	spawner["SpawnData"]["id"] = TAG_String(spawnName)
	
	return spawner
	
	
#Places block
def setBlock(level, (block, data), x, y, z):
	level.setBlockAt(x, y, z, block)
	level.setBlockDataAt(x, y, z, data)
	
	
# picks a "random" key/Item_block from a written distribution
def pickblock(cump, size): 
	r = random.random() * size
	
	for key, value in cump.iteritems():
		low, high = value
		if r >= low and r < high:
			return key
	
def pickItem(cump, size):
	r = random.random() * size
	
	for key, value in cump.iteritems():
		low, high = value
		if r >= low and r < high:
			return key

def pickSpawn(cump, size):
	r = random.random() * size
	
	for key, value in cump.iteritems():
		low, high = value
		if r >= low and r < high:
			return key
	
	
# Spawner distributions
def overworldSpawns():
	#[MinecraftId"] = lower number is more rare
	pspawn = {}
	pspawn["minecraft:cow"] = 30
	pspawn["minecraft:creeper"] = 100
	pspawn["minecraft:skeleton"] = 100
	pspawn["minecraft:spider"] = 100
	pspawn["minecraft:cave_spider"] = 100
	pspawn["minecraft:zombie"] = 100
	pspawn["minecraft:slime"] = 20
	pspawn["minecraft:sheep"] = 50
	pspawn["minecraft:chicken"] = 35
	pspawn["minecraft:squid"] = 10
	pspawn["minecraft:wolf"] = 20
	pspawn["minecraft:enderman"] = 5
	pspawn["minecraft:silverfish"] = 5
	pspawn["minecraft:villager"] = 5
	pspawn["minecraft:mushroom"] = 30
	pspawn["minecraft:ocelot"] = 10
	pspawn["minecraft:witch"] = 40
	pspawn["minecraft:polar_bear"] = 28
	pspawn["minecraft:rabbit"] = 30
	pspawn["minecraft:elder_guardian"] = 40
	pspawn["minecraft:guardian"] = 40
	pspawn["minecraft:husk"] = 100
	pspawn["minecraft:stray"] = 100
	pspawn["minecraft:vex"] = 1
	pspawn["minecraft:vindicator"] = 1
	pspawn["minecraft:horse"] = 13
	pspawn["minecraft:donkey"] = 13
	pspawn["minecraft:llama"] = 35
	pspawn["minecraft:villager_golem"] = 3
	return pspawn

def netherSpawns():
	pspawn = {}
	pspawn["minecraft:zombie_pigman"] = 200
	pspawn["minecraft:blaze"] = 100
	pspawn["minecraft:magma_cube"] = 40
	pspawn["minecraft:skeleton"] = 20
	pspawn["minecraft:ghast"] = 100
	pspawn["minecraft:enderman"] = 20
	return pspawn
			
def endSpawns():
	pspawn = {}
	pspawn["minecraft:shulker"] = 200
	pspawn["minecraft:enderman"] = 1000
	pspawn["minecraft:endermite"] = 50
	return pspawn

def normalSpawns():
	pspawn = {}
	pspawn["minecraft:cow"] = 40
	pspawn["minecraft:creeper"] = 100
	pspawn["minecraft:skeleton"] = 100
	pspawn["minecraft:spider"] = 100
	pspawn["minecraft:cave_spider"] = 100
	pspawn["minecraft:zombie"] = 100
	pspawn["minecraft:sheep"] = 50
	pspawn["minecraft:chicken"] = 36
	pspawn["minecraft:wolf"] = 30
	pspawn["minecraft:silverfish"] = 15
	pspawn["minecraft:villager"] = 10
	pspawn["minecraft:rabbit"] = 100
	pspawn["minecraft:horse"] = 100
	pspawn["minecraft:donkey"] = 100
	pspawn["minecraft:llama"] = 100
	return pspawn
	
def iceSpawns():
	pspawn = {}
	pspawn["minecraft:wolf"] = 60
	pspawn["minecraft:ocelot"] = 20
	pspawn["minecraft:polar_bear"] = 100
	pspawn["minecraft:rabbit"] = 75
	pspawn["minecraft:stray"] = 30
	pspawn["minecraft:vex"] = 1
	pspawn["minecraft:vindicator"] = 1
	pspawn["minecraft:donkey"] = 25
	pspawn["minecraft:llama"] = 25
	pspawn["minecraft:villager_golem"] = 25
	return pspawn
	
def jungleSpawns():
	pspawn = {}
	pspawn["minecraft:creeper"] = 130
	pspawn["minecraft:skeleton"] = 200
	pspawn["minecraft:zombie"] = 100
	pspawn["minecraft:chicken"] = 10
	pspawn["minecraft:wolf"] = 100
	pspawn["minecraft:ocelot"] = 200
	pspawn["minecraft:witch"] = 20
	pspawn["minecraft:villager_golem"] = 10
	return pspawn
	
def swampSpawns():
	pspawn = {}
	pspawn["minecraft:creeper"] = 100
	pspawn["minecraft:slime"] = 500
	pspawn["minecraft:squid"] = 20
	pspawn["minecraft:villager"] = 150
	pspawn["minecraft:ocelot"] = 100
	pspawn["minecraft:witch"] = 250
	pspawn["minecraft:stray"] = 200
	pspawn["minecraft:vex"] = 1
	pspawn["minecraft:vindicator"] = 1
	return pspawn
	
def desertSpawns():
	pspawn = {}
	pspawn["minecraft:creeper"] = 45
	pspawn["minecraft:skeleton"] = 100
	pspawn["minecraft:spider"] = 100
	pspawn["minecraft:stray"] = 200
	pspawn["minecraft:cave_spider"] = 75
	pspawn["minecraft:zombie"] = 100
	pspawn["minecraft:donkey"] = 300
	return pspawn
	
def oceanSpawns():
	pspawn = {}
	pspawn["minecraft:squid"] = 300
	pspawn["minecraft:elder_guardian"] = 100
	pspawn["minecraft:guardian"] = 100
	return pspawn
	
def mushroomSpawns():
	pspawn = {}
	pspawn["minecraft:cow"] = 5
	pspawn["minecraft:creeper"] = 30
	pspawn["minecraft:skeleton"] = 30
	pspawn["minecraft:spider"] = 30
	pspawn["minecraft:mushroom"] = 100
	pspawn["minecraft:villager_golem"] = 75
	return pspawn
	
def mesaSpawns():
	pspawn = {}
	pspawn["minecraft:creeper"] = 100
	pspawn["minecraft:skeleton"] = 100
	pspawn["minecraft:spider"] = 75
	pspawn["minecraft:zombie"] = 100
	return pspawn
	
def overloadedSpawns():
	pspawn = {}
	pspawn["minecraft:cow"] = 100
	pspawn["minecraft:creeper"] = 100
	pspawn["minecraft:skeleton"] = 100
	pspawn["minecraft:spider"] = 100
	pspawn["minecraft:cave_spider"] = 100
	pspawn["minecraft:zombie"] = 100
	pspawn["minecraft:slime"] = 100
	pspawn["minecraft:sheep"] = 100
	pspawn["minecraft:chicken"] = 100
	pspawn["minecraft:squid"] = 100
	pspawn["minecraft:wolf"] = 100
	pspawn["minecraft:enderman"] = 100
	pspawn["minecraft:silverfish"] = 100
	pspawn["minecraft:villager"] = 100
	pspawn["minecraft:mushroom"] = 100
	pspawn["minecraft:ocelot"] = 100
	pspawn["minecraft:witch"] = 100
	pspawn["minecraft:polar_bear"] = 100
	pspawn["minecraft:rabbit"] = 100
	pspawn["minecraft:elder_guardian"] = 100
	pspawn["minecraft:guardian"] = 100
	pspawn["minecraft:husk"] = 100
	pspawn["minecraft:stray"] = 100
	pspawn["minecraft:vex"] = 10
	pspawn["minecraft:vindicator"] = 10
	pspawn["minecraft:horse"] = 100
	pspawn["minecraft:donkey"] = 100
	pspawn["minecraft:llama"] = 100
	pspawn["minecraft:villager_golem"] = 100
	return pspawn
	
	
# Chest loot distributions
def overworldChestLoot(options):
	# ["minecraftId",quantity] = lower number is more rare
	pitems = {}
	pitems["minecraft:air",0,random.randint(1, 1)] = 9000
	pitems["minecraft:cobblestone",0,random.randint(1, 64)] = 100
	pitems["minecraft:sapling",0,random.randint(1, 5)] = 100 #Oak
	pitems["minecraft:sapling",1,random.randint(1, 5)] = 100 #Spruce
	pitems["minecraft:sapling",2,random.randint(1, 5)] = 100 #Birch
	pitems["minecraft:sapling",3,random.randint(1, 5)] = 100 #Jungle
	pitems["minecraft:sapling",4,random.randint(1, 5)] = 100 #Acacia
	pitems["minecraft:sapling",5,random.randint(1, 5)] = 100 #Dark oak
	pitems["minecraft:log",0,random.randint(1, 15)] = 100 #Oak
	pitems["minecraft:log",1,random.randint(1, 15)] = 100 #Spruce
	pitems["minecraft:log",2,random.randint(1, 15)] = 100 #Birch
	pitems["minecraft:log",3,random.randint(1, 15)] = 100 #Jungle
	pitems["minecraft:golden_rail",0,random.randint(1, 10)] = 100
	pitems["minecraft:detector_rail",0,random.randint(1, 10)] = 100
	pitems["minecraft:ladder",0,random.randint(1, 5)] = 100
	pitems["minecraft:rail",0,random.randint(1, 15)] = 100
	pitems["minecraft:cactus",0,random.randint(4, 10)] = 300
	pitems["minecraft:vine",0,random.randint(1, 15)] = 100
	pitems["minecraft:waterlily",0,random.randint(1, 4)] = 100
	pitems["minecraft:log2",0,random.randint(1, 5)] = 100 #Acacia
	pitems["minecraft:log2",1,random.randint(1, 5)] = 100 #Dark
	pitems["minecraft:iron_shovel",0,random.randint(1, 1)] = 100
	pitems["minecraft:iron_pickaxe",0,random.randint(1, 1)] = 100
	pitems["minecraft:iron_axe",0,random.randint(1, 1)] = 100
	pitems["minecraft:apple",0,random.randint(1, 10)] = 100
	pitems["minecraft:bow",0,random.randint(1, 1)] = 100
	pitems["minecraft:arrow",0,random.randint(1, 12)] = 100
	pitems["minecraft:coal",0,random.randint(1, 6)] = 100
	pitems["minecraft:diamond",0,random.randint(1, 2)] = 50
	pitems["minecraft:iron_ingot",0,random.randint(1, 4)] = 50
	pitems["minecraft:gold_ingot",0,random.randint(1, 2)] = 50
	pitems["minecraft:iron_sword",0,random.randint(1, 1)] = 50
	pitems["minecraft:diamond_sword",0,random.randint(1, 1)] = 50
	pitems["minecraft:diamond_shovel",0,random.randint(1, 1)] = 50
	pitems["minecraft:diamond_pickaxe",0,random.randint(1, 1)] = 50
	pitems["minecraft:diamond_axe",0,random.randint(1, 1)] = 50
	pitems["minecraft:feather",0,random.randint(1, 5)] = 100
	pitems["minecraft:gunpowder",0,random.randint(1, 3)] = 100
	pitems["minecraft:wheat_seeds",0,random.randint(1, 5)] = 100
	pitems["minecraft:wheat",0,random.randint(1, 4)] = 100
	pitems["minecraft:bread",0,random.randint(1, 4)] = 100
	pitems["minecraft:iron_helmet",0,random.randint(1, 1)] = 50
	pitems["minecraft:iron_chestplate",0,random.randint(1, 1)] = 50
	pitems["minecraft:iron_leggings",0,random.randint(1, 1)] = 50
	pitems["minecraft:iron_boots",0,random.randint(1, 1)] = 50
	pitems["minecraft:diamond_helmet",0,random.randint(1, 1)] = 50
	pitems["minecraft:diamond_chestplate",0,random.randint(1, 1)] = 50
	pitems["minecraft:diamond_leggings",0,random.randint(1, 1)] = 50
	pitems["minecraft:diamond_boots",0,random.randint(1, 1)] = 50
	pitems["minecraft:porkchop",0,random.randint(1, 5)] = 100
	pitems["minecraft:cooked_porkchop",0,random.randint(1, 2)] = 100
	pitems["minecraft:golden_apple",0,random.randint(1, 2)] = 25
	pitems["minecraft:golden_apple",1,random.randint(1, 1)] = 25
	pitems["minecraft:water_bucket",0,random.randint(1, 1)] = 100
	pitems["minecraft:lava_bucket",0,random.randint(1, 1)] = 100
	pitems["minecraft:saddle",0,random.randint(1, 1)] = 100
	pitems["minecraft:leather",0,random.randint(1, 4)] = 100
	pitems["minecraft:reeds",0,random.randint(1, 5)] = 100
	pitems["minecraft:dye",1,random.randint(1, 4)] = 100  #rose red
	pitems["minecraft:dye",3,random.randint(1, 4)] = 100  #coco beans
	pitems["minecraft:dye",5,random.randint(1, 4)] = 100  #Purple dye
	pitems["minecraft:dye",6,random.randint(1, 4)] = 100  #Cyan dye
	pitems["minecraft:dye",7,random.randint(1, 4)] = 100  #Light gray
	pitems["minecraft:dye",8,random.randint(1, 4)] = 100  #Gray
	pitems["minecraft:dye",9,random.randint(1, 4)] = 100  #pink
	pitems["minecraft:dye",10,random.randint(1, 4)] = 100 #lime
	pitems["minecraft:dye",11,random.randint(1, 4)] = 100 #dandelion
	pitems["minecraft:dye",12,random.randint(1, 4)] = 100 #Light blue
	pitems["minecraft:dye",13,random.randint(1, 4)] = 100 #Magenta
	pitems["minecraft:dye",14,random.randint(1, 4)] = 100 #orange
	pitems["minecraft:bed",0,random.randint(1, 1)] = 100
	pitems["minecraft:melon",0,random.randint(1, 4)] = 100
	pitems["minecraft:pumpkin_seeds",0,random.randint(1, 3)] = 100
	pitems["minecraft:melon_seeds",0,random.randint(1, 3)] = 100
	pitems["minecraft:beef",0,random.randint(1, 4)] = 100
	pitems["minecraft:cooked_beef",0,random.randint(1, 2)] = 100
	pitems["minecraft:chicken",0,random.randint(1, 4)] = 100
	pitems["minecraft:cooked_chicken",0,random.randint(1, 2)] = 100
	pitems["minecraft:ender_pearl",0,random.randint(1, 10)] = 100
	pitems["minecraft:speckled_melon",0,random.randint(1, 3)] = 100
	pitems["minecraft:experience_bottle",0,random.randint(1, 32)] = 400
	pitems["minecraft:carrot",0,random.randint(1, 5)] = 100
	pitems["minecraft:potato",0,random.randint(1, 5)] = 100
	pitems["minecraft:golden_carrot",0,random.randint(1, 2)] = 100
	pitems["minecraft:nether_star",0,random.randint(1, 1)] = 100
	pitems["minecraft:mutton",0,random.randint(1, 5)] = 100
	pitems["minecraft:cooked_mutton",0,random.randint(1, 2)] = 100
	pitems["minecraft:beetroot",0,random.randint(1, 2)] = 100
	if options["Game version"] == "1.12+":
		pitems["minecraft:concrete",0,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",1,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",2,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",3,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",4,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",5,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",6,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",7,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",8,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",9,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",10,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",11,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",12,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",13,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",14,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",15,random.randint(2, 8)] = 10
	return pitems
			
def netherChestLoot(options):
	pitems = {}
	pitems["minecraft:air",0,random.randint(1, 1)] = 4000
	pitems["minecraft:diamond",0,random.randint(1, 2)] = 75
	pitems["minecraft:iron_ingot",0,random.randint(1, 4)] = 75
	pitems["minecraft:gold_ingot",0,random.randint(1, 2)] = 75
	pitems["minecraft:diamond_sword",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_pickaxe",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_axe",0,random.randint(1, 1)] = 75
	pitems["minecraft:chainmail_helmet",0,random.randint(1, 1)] = 110
	pitems["minecraft:chainmail_chestplate",0,random.randint(1, 1)] = 110
	pitems["minecraft:chainmail_leggings",0,random.randint(1, 1)] = 110
	pitems["minecraft:chainmail_boots",0,random.randint(1, 1)] = 110
	pitems["minecraft:diamond_helmet",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_chestplate",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_leggings",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_boots",0,random.randint(1, 1)] = 75
	pitems["minecraft:golden_apple",0,random.randint(1, 2)] = 100
	pitems["minecraft:golden_apple",1,random.randint(1, 1)] = 100
	pitems["minecraft:lava_bucket",0,random.randint(1, 1)] = 100
	pitems["minecraft:saddle",0,random.randint(1, 1)] = 100
	pitems["minecraft:glowstone_dust",0,random.randint(1, 7)] = 150
	pitems["minecraft:blaze_rod",0,random.randint(1, 5)] = 175
	pitems["minecraft:ghast_tear",0,random.randint(1, 3)] = 25
	pitems["minecraft:gold_nugget",0,random.randint(1, 15)] = 200
	pitems["minecraft:nether_wart",0,random.randint(1, 4)] = 200
	pitems["minecraft:fermented_spider_eye",0,random.randint(1, 1)] = 100
	pitems["minecraft:magma_cream",0,random.randint(1, 5)] = 100
	pitems["minecraft:experience_bottle",0,random.randint(1, 32)] = 700
	pitems["minecraft:iron_horse_armor",0,random.randint(1, 1)] = 100
	pitems["minecraft:golden_horse_armor",0,random.randint(1, 1)] = 100
	pitems["minecraft:diamond_horse_armor",0,random.randint(1, 1)] = 100
	pitems["minecraft:lead",0,random.randint(1, 4)] = 100
	pitems["minecraft:name_tag",0,random.randint(1, 7)] = 100
	pitems["minecraft:dye",1,random.randint(1, 4)] = 100  #rose red
	pitems["minecraft:dye",14,random.randint(1, 4)] = 100 #Inc sack
	return pitems
			
def endChestLoot(options):
	pitems = {}
	pitems["minecraft:air",0,random.randint(1, 1)] = 7300
	pitems["minecraft:white_shulker_box",0,random.randint(1, 1)] = 30
	pitems["minecraft:orange_shulker_box",0,random.randint(1, 1)] = 30
	pitems["minecraft:magenta_shulker_box",0,random.randint(1, 1)] = 30
	pitems["minecraft:light_blue_shulker_box",0,random.randint(1, 1)] = 30
	pitems["minecraft:yellow_shulker_box",0,random.randint(1, 1)] = 30
	pitems["minecraft:lime_shulker_box",0,random.randint(1, 1)] = 30
	pitems["minecraft:pink_shulker_box",0,random.randint(1, 1)] = 30
	pitems["minecraft:gray_shulker_box",0,random.randint(1, 1)] = 30
	pitems["minecraft:silver_shulker_box",0,random.randint(1, 1)] = 30
	pitems["minecraft:cyan_shulker_box",0,random.randint(1, 1)] = 30
	pitems["minecraft:purple_shulker_box",0,random.randint(1, 1)] = 30
	pitems["minecraft:blue_shulker_box",0,random.randint(1, 1)] = 30
	pitems["minecraft:brown_shulker_box",0,random.randint(1, 1)] = 30
	pitems["minecraft:green_shulker_box",0,random.randint(1, 1)] = 30
	pitems["minecraft:red_shulker_box",0,random.randint(1, 1)] = 30
	pitems["minecraft:black_shulker_box",0,random.randint(1, 1)] = 30
	pitems["minecraft:diamond",0,random.randint(1, 2)] = 200
	pitems["minecraft:iron_ingot",0,random.randint(1, 4)] = 200
	pitems["minecraft:gold_ingot",0,random.randint(1, 2)] = 100
	pitems["minecraft:diamond_sword",0,random.randint(1, 1)] = 100
	pitems["minecraft:diamond_shovel",0,random.randint(1, 1)] = 100
	pitems["minecraft:diamond_pickaxe",0,random.randint(1, 1)] = 100
	pitems["minecraft:diamond_axe",0,random.randint(1, 1)] = 100
	pitems["minecraft:diamond_helmet",0,random.randint(1, 1)] = 100
	pitems["minecraft:diamond_chestplate",0,random.randint(1, 1)] = 100
	pitems["minecraft:diamond_leggings",0,random.randint(1, 1)] = 100
	pitems["minecraft:diamond_boots",0,random.randint(1, 1)] = 100
	pitems["minecraft:experience_bottle",0,random.randint(1, 32)] = 1000
	pitems["minecraft:nether_star",0,random.randint(1, 1)] = 20
	pitems["minecraft:name_tag",0,random.randint(1, 7)] = 100
	pitems["minecraft:chorus_fruit",0,random.randint(1, 3)] = 2000
	pitems["minecraft:popped_chorus_fruit",0,random.randint(1, 15)] = 2000
	pitems["minecraft:dragon_breath",0,random.randint(1, 5)] = 100
	pitems["minecraft:spectral_arrow",0,random.randint(4, 8)] = 100
	pitems["minecraft:tipped_arrow",0,random.randint(4, 10)] = 100
	pitems["minecraft:elytra",0,random.randint(1, 1)] = 150
	pitems["minecraft:totem_of_undying",0,random.randint(1, 1)] = 150
	pitems["minecraft:dye",6,random.randint(1, 4)] = 100  #Cyan dye
	pitems["minecraft:dye",7,random.randint(1, 4)] = 100  #Light gray
	pitems["minecraft:dye",8,random.randint(1, 4)] = 100  #Gray
	pitems["minecraft:dye",12,random.randint(1, 4)] = 100 #Light blue
	return pitems
	
def normalChestLoot(options):
	pitems = {}
	pitems["minecraft:air",0,random.randint(1, 1)] = 7000
	pitems["minecraft:cobblestone",0,random.randint(1, 64)] = 100
	pitems["minecraft:sapling",0,random.randint(1, 5)] = 100 #Oak
	pitems["minecraft:sapling",1,random.randint(1, 5)] = 100 #Spruce
	pitems["minecraft:sapling",2,random.randint(1, 5)] = 100 #Birch
	pitems["minecraft:sapling",3,random.randint(1, 5)] = 100 #Jungle
	pitems["minecraft:sapling",4,random.randint(1, 5)] = 100 #Acacia
	pitems["minecraft:sapling",5,random.randint(1, 5)] = 100 #Dark oak
	pitems["minecraft:log",0,random.randint(1, 15)] = 75 #Oak
	pitems["minecraft:log",1,random.randint(1, 15)] = 75 #Spruce
	pitems["minecraft:log",2,random.randint(1, 15)] = 75 #Birch
	pitems["minecraft:log",3,random.randint(1, 15)] = 75 #Jungle
	pitems["minecraft:golden_rail",0,random.randint(1, 10)] = 25
	pitems["minecraft:detector_rail",0,random.randint(1, 10)] = 25
	pitems["minecraft:yellow_flower",0,random.randint(1, 12)] = 25
	pitems["minecraft:red_flower",0,random.randint(1, 12)] = 25
	pitems["minecraft:red_flower",1,random.randint(1, 12)] = 25
	pitems["minecraft:red_flower",2,random.randint(1, 12)] = 25
	pitems["minecraft:red_flower",3,random.randint(1, 12)] = 25
	pitems["minecraft:red_flower",4,random.randint(1, 12)] = 25
	pitems["minecraft:red_flower",5,random.randint(1, 12)] = 25
	pitems["minecraft:red_flower",6,random.randint(1, 12)] = 25
	pitems["minecraft:red_flower",7,random.randint(1, 12)] = 25
	pitems["minecraft:red_flower",8,random.randint(1, 12)] = 25
	pitems["minecraft:ladder",0,random.randint(1, 5)] = 100
	pitems["minecraft:rail",0,random.randint(1, 15)] = 100
	pitems["minecraft:apple",0,random.randint(1, 10)] = 100
	pitems["minecraft:bow",0,random.randint(1, 1)] = 100
	pitems["minecraft:arrow",0,random.randint(1, 12)] = 100
	pitems["minecraft:coal",0,random.randint(1, 6)] = 70
	pitems["minecraft:diamond",0,random.randint(1, 2)] = 30
	pitems["minecraft:iron_ingot",0,random.randint(1, 4)] = 75
	pitems["minecraft:gold_ingot",0,random.randint(1, 2)] = 50
	pitems["minecraft:diamond_sword",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_shovel",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_pickaxe",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_axe",0,random.randint(1, 1)] = 75
	pitems["minecraft:feather",0,random.randint(1, 5)] = 100
	pitems["minecraft:gunpowder",0,random.randint(1, 3)] = 100
	pitems["minecraft:wheat_seeds",0,random.randint(1, 5)] = 100
	pitems["minecraft:wheat",0,random.randint(1, 4)] = 100
	pitems["minecraft:bread",0,random.randint(1, 4)] = 100
	pitems["minecraft:iron_helmet",0,random.randint(1, 1)] = 75
	pitems["minecraft:iron_chestplate",0,random.randint(1, 1)] = 75
	pitems["minecraft:iron_leggings",0,random.randint(1, 1)] = 75
	pitems["minecraft:iron_boots",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_helmet",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_chestplate",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_leggings",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_boots",0,random.randint(1, 1)] = 75
	pitems["minecraft:porkchop",0,random.randint(1, 5)] = 100
	pitems["minecraft:cooked_porkchop",0,random.randint(1, 2)] = 100
	pitems["minecraft:golden_apple",0,random.randint(1, 2)] = 15
	pitems["minecraft:golden_apple",1,random.randint(1, 1)] = 20
	pitems["minecraft:water_bucket",0,random.randint(1, 1)] = 100
	pitems["minecraft:lava_bucket",0,random.randint(1, 1)] = 100
	pitems["minecraft:reeds",0,random.randint(1, 5)] = 100
	pitems["minecraft:dye",0,random.randint(1, 4)] = 40   #ink sac
	pitems["minecraft:dye",1,random.randint(1, 4)] = 100  #rose red
	pitems["minecraft:dye",5,random.randint(1, 4)] = 100  #Purple dye
	pitems["minecraft:dye",6,random.randint(1, 4)] = 100  #Cyan dye
	pitems["minecraft:dye",7,random.randint(1, 4)] = 100  #Light gray
	pitems["minecraft:dye",8,random.randint(1, 4)] = 100  #Gray
	pitems["minecraft:dye",9,random.randint(1, 4)] = 100  #pink
	pitems["minecraft:dye",10,random.randint(1, 4)] = 100 #lime
	pitems["minecraft:dye",11,random.randint(1, 4)] = 100 #dandelion
	pitems["minecraft:dye",12,random.randint(1, 4)] = 100 #Light blue
	pitems["minecraft:dye",13,random.randint(1, 4)] = 100 #Magenta
	pitems["minecraft:dye",14,random.randint(1, 4)] = 100 #orange
	pitems["minecraft:bed",0,random.randint(1, 1)] = 100
	pitems["minecraft:beef",0,random.randint(1, 4)] = 100
	pitems["minecraft:cooked_beef",0,random.randint(1, 2)] = 100
	pitems["minecraft:chicken",0,random.randint(1, 4)] = 100
	pitems["minecraft:cooked_chicken",0,random.randint(1, 2)] = 100
	pitems["minecraft:ender_pearl",0,random.randint(1, 10)] = 100
	pitems["minecraft:speckled_melon",0,random.randint(1, 3)] = 100
	pitems["minecraft:experience_bottle",0,random.randint(1, 32)] = 550
	pitems["minecraft:carrot",0,random.randint(1, 5)] = 100
	pitems["minecraft:potato",0,random.randint(1, 5)] = 100
	pitems["minecraft:mutton",0,random.randint(1, 5)] = 100
	pitems["minecraft:cooked_mutton",0,random.randint(1, 2)] = 100
	if options["Game version"] == "1.12+":
		pitems["minecraft:concrete",0,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",1,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",2,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",3,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",4,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",5,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",6,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",7,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",8,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",9,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",10,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",11,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",12,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",13,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",14,random.randint(2, 8)] = 10
		pitems["minecraft:concrete",15,random.randint(2, 8)] = 10
	return pitems
	
def iceChestLoot(options):
	pitems = {}
	pitems["minecraft:air",0,random.randint(1, 1)] = 2500
	pitems["minecraft:apple",0,random.randint(1, 10)] = 100
	pitems["minecraft:bow",0,random.randint(1, 1)] = 100
	pitems["minecraft:arrow",0,random.randint(1, 12)] = 100
	pitems["minecraft:coal",0,random.randint(1, 6)] = 100
	pitems["minecraft:diamond",0,random.randint(1, 2)] = 50
	pitems["minecraft:iron_ingot",0,random.randint(1, 4)] = 60
	pitems["minecraft:gold_ingot",0,random.randint(1, 2)] = 70
	pitems["minecraft:iron_sword",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_sword",0,random.randint(1, 1)] = 60
	pitems["minecraft:diamond_shovel",0,random.randint(1, 1)] = 60
	pitems["minecraft:diamond_pickaxe",0,random.randint(1, 1)] = 60
	pitems["minecraft:diamond_axe",0,random.randint(1, 1)] = 60
	pitems["minecraft:iron_helmet",0,random.randint(1, 1)] = 80
	pitems["minecraft:iron_chestplate",0,random.randint(1, 1)] = 80
	pitems["minecraft:iron_leggings",0,random.randint(1, 1)] = 80
	pitems["minecraft:iron_boots",0,random.randint(1, 1)] = 80
	pitems["minecraft:diamond_helmet",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_chestplate",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_leggings",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_boots",0,random.randint(1, 1)] = 75
	pitems["minecraft:porkchop",0,random.randint(1, 5)] = 100
	pitems["minecraft:cooked_porkchop",0,random.randint(1, 2)] = 100
	pitems["minecraft:golden_apple",0,random.randint(1, 2)] = 100
	pitems["minecraft:golden_apple",1,random.randint(1, 1)] = 100
	pitems["minecraft:experience_bottle",0,random.randint(1, 32)] = 500
	pitems["minecraft:dye",7,random.randint(1, 4)] = 100  #Light gray
	pitems["minecraft:dye",12,random.randint(1, 4)] = 100 #Light blue
	pitems["minecraft:dye",13,random.randint(1, 4)] = 100 #Magenta
	return pitems
	
def jungleChestLoot(options):
	pitems = {}
	pitems["minecraft:air",0,random.randint(1, 1)] = 6500
	pitems["minecraft:cobblestone",0,random.randint(1, 64)] = 100
	pitems["minecraft:sapling",0,random.randint(1, 5)] = 75 #Oak
	pitems["minecraft:sapling",3,random.randint(1, 5)] = 75 #Jungle
	pitems["minecraft:log",0,random.randint(1, 15)] = 100 #Oak
	pitems["minecraft:log",3,random.randint(1, 15)] = 100 #Jungle
	pitems["minecraft:yellow_flower",0,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",0,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",1,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",2,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",3,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",4,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",5,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",6,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",7,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",8,random.randint(1, 12)] = 100
	pitems["minecraft:vine",0,random.randint(1, 15)] = 100
	pitems["minecraft:iron_shovel",0,random.randint(1, 1)] = 100
	pitems["minecraft:iron_pickaxe",0,random.randint(1, 1)] = 100
	pitems["minecraft:iron_axe",0,random.randint(1, 1)] = 100
	pitems["minecraft:apple",0,random.randint(1, 10)] = 100
	pitems["minecraft:bow",0,random.randint(1, 1)] = 100
	pitems["minecraft:arrow",0,random.randint(1, 12)] = 100
	pitems["minecraft:coal",0,random.randint(1, 6)] = 100
	pitems["minecraft:diamond",0,random.randint(1, 2)] = 40
	pitems["minecraft:iron_ingot",0,random.randint(1, 4)] = 65
	pitems["minecraft:gold_ingot",0,random.randint(1, 2)] = 55
	pitems["minecraft:iron_sword",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_sword",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_shovel",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_pickaxe",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_axe",0,random.randint(1, 1)] = 75
	pitems["minecraft:feather",0,random.randint(1, 5)] = 100
	pitems["minecraft:wheat_seeds",0,random.randint(1, 5)] = 100
	pitems["minecraft:wheat",0,random.randint(1, 4)] = 100
	pitems["minecraft:bread",0,random.randint(1, 4)] = 100
	pitems["minecraft:iron_helmet",0,random.randint(1, 1)] = 90
	pitems["minecraft:iron_chestplate",0,random.randint(1, 1)] = 90
	pitems["minecraft:iron_leggings",0,random.randint(1, 1)] = 90
	pitems["minecraft:iron_boots",0,random.randint(1, 1)] = 90
	pitems["minecraft:diamond_helmet",0,random.randint(1, 1)] = 50
	pitems["minecraft:diamond_chestplate",0,random.randint(1, 1)] = 50
	pitems["minecraft:diamond_leggings",0,random.randint(1, 1)] = 50
	pitems["minecraft:diamond_boots",0,random.randint(1, 1)] = 50
	pitems["minecraft:porkchop",0,random.randint(1, 5)] = 100
	pitems["minecraft:cooked_porkchop",0,random.randint(1, 2)] = 100
	pitems["minecraft:golden_apple",0,random.randint(1, 2)] = 25
	pitems["minecraft:golden_apple",1,random.randint(1, 1)] = 10
	pitems["minecraft:water_bucket",0,random.randint(1, 1)] = 100
	pitems["minecraft:lava_bucket",0,random.randint(1, 1)] = 100
	pitems["minecraft:reeds",0,random.randint(1, 5)] = 100
	pitems["minecraft:dye",3,random.randint(1, 4)] = 100  #coco beans
	pitems["minecraft:dye",10,random.randint(1, 4)] = 100 #lime
	pitems["minecraft:dye",11,random.randint(1, 4)] = 100 #dandelion
	pitems["minecraft:bed",0,random.randint(1, 1)] = 100
	pitems["minecraft:melon",0,random.randint(1, 4)] = 100
	pitems["minecraft:pumpkin_seeds",0,random.randint(1, 3)] = 100
	pitems["minecraft:melon_seeds",0,random.randint(1, 3)] = 100
	pitems["minecraft:beef",0,random.randint(1, 4)] = 100
	pitems["minecraft:cooked_beef",0,random.randint(1, 2)] = 100
	pitems["minecraft:speckled_melon",0,random.randint(1, 3)] = 100
	pitems["minecraft:experience_bottle",0,random.randint(1, 32)] = 500
	pitems["minecraft:totem_of_undying",0,random.randint(1, 1)] = 5
	return pitems
	
def swampChestLoot(options):
	pitems = {}
	pitems["minecraft:air",0,random.randint(1, 1)] = 3000
	pitems["minecraft:cobblestone",0,random.randint(1, 64)] = 100
	pitems["minecraft:sapling",1,random.randint(1, 5)] = 100 #Spruce
	pitems["minecraft:sapling",2,random.randint(1, 5)] = 100 #Birch
	pitems["minecraft:log",2,random.randint(1, 15)] = 100 #Birch
	pitems["minecraft:waterlily",0,random.randint(1, 4)] = 400
	pitems["minecraft:iron_shovel",0,random.randint(1, 1)] = 100
	pitems["minecraft:iron_pickaxe",0,random.randint(1, 1)] = 100
	pitems["minecraft:iron_axe",0,random.randint(1, 1)] = 100
	pitems["minecraft:apple",0,random.randint(1, 10)] = 200
	pitems["minecraft:bow",0,random.randint(1, 1)] = 100
	pitems["minecraft:arrow",0,random.randint(1, 12)] = 100
	pitems["minecraft:coal",0,random.randint(1, 6)] = 100
	pitems["minecraft:diamond",0,random.randint(1, 2)] = 50
	pitems["minecraft:iron_ingot",0,random.randint(1, 4)] = 75
	pitems["minecraft:gold_ingot",0,random.randint(1, 2)] = 55
	pitems["minecraft:iron_sword",0,random.randint(1, 1)] = 80
	pitems["minecraft:diamond_sword",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_shovel",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_pickaxe",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_axe",0,random.randint(1, 1)] = 75
	pitems["minecraft:bread",0,random.randint(1, 4)] = 100
	pitems["minecraft:porkchop",0,random.randint(1, 5)] = 100
	pitems["minecraft:cooked_porkchop",0,random.randint(1, 2)] = 100
	pitems["minecraft:golden_apple",0,random.randint(1, 2)] = 100
	pitems["minecraft:golden_apple",1,random.randint(1, 1)] = 100
	pitems["minecraft:water_bucket",0,random.randint(1, 1)] = 100
	pitems["minecraft:experience_bottle",0,random.randint(1, 32)] = 400
	pitems["minecraft:dye",0,random.randint(1, 4)] = 100 #ink sac
	return pitems
	
def desertChestLoot(options):
	pitems = {}
	pitems["minecraft:air",0,random.randint(1, 1)] = 5200
	pitems["minecraft:cobblestone",0,random.randint(1, 64)] = 100
	pitems["minecraft:sapling",4,random.randint(1, 5)] = 100 #Acacia sapling
	pitems["minecraft:cactus",0,random.randint(2, 10)] = 500
	pitems["minecraft:log2",0,random.randint(1, 5)] = 100 #Acacia
	pitems["minecraft:iron_shovel",0,random.randint(1, 1)] = 80
	pitems["minecraft:iron_pickaxe",0,random.randint(1, 1)] = 80
	pitems["minecraft:iron_axe",0,random.randint(1, 1)] = 100
	pitems["minecraft:apple",0,random.randint(1, 10)] = 100
	pitems["minecraft:bow",0,random.randint(1, 1)] = 100
	pitems["minecraft:arrow",0,random.randint(1, 12)] = 100
	pitems["minecraft:coal",0,random.randint(1, 6)] = 100
	pitems["minecraft:diamond",0,random.randint(1, 2)] = 50
	pitems["minecraft:iron_ingot",0,random.randint(1, 4)] = 80
	pitems["minecraft:gold_ingot",0,random.randint(1, 2)] = 65
	pitems["minecraft:diamond_sword",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_shovel",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_pickaxe",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_axe",0,random.randint(1, 1)] = 75
	pitems["minecraft:feather",0,random.randint(1, 5)] = 100
	pitems["minecraft:gunpowder",0,random.randint(1, 3)] = 100
	pitems["minecraft:wheat_seeds",0,random.randint(1, 5)] = 100
	pitems["minecraft:wheat",0,random.randint(1, 4)] = 100
	pitems["minecraft:bread",0,random.randint(1, 4)] = 100
	pitems["minecraft:iron_helmet",0,random.randint(1, 1)] = 85
	pitems["minecraft:iron_chestplate",0,random.randint(1, 1)] = 85
	pitems["minecraft:iron_leggings",0,random.randint(1, 1)] = 85
	pitems["minecraft:iron_boots",0,random.randint(1, 1)] = 85
	pitems["minecraft:diamond_helmet",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_chestplate",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_leggings",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_boots",0,random.randint(1, 1)] = 75
	pitems["minecraft:porkchop",0,random.randint(1, 5)] = 100
	pitems["minecraft:cooked_porkchop",0,random.randint(1, 2)] = 100
	pitems["minecraft:golden_apple",0,random.randint(1, 2)] = 100
	pitems["minecraft:golden_apple",1,random.randint(1, 1)] = 100
	pitems["minecraft:lava_bucket",0,random.randint(1, 1)] = 100
	pitems["minecraft:saddle",0,random.randint(1, 1)] = 100
	pitems["minecraft:leather",0,random.randint(1, 4)] = 100
	pitems["minecraft:reeds",0,random.randint(1, 5)] = 100
	pitems["minecraft:dye",2,random.randint(1, 4)] = 100  #cactus green
	pitems["minecraft:dye",14,random.randint(1, 4)] = 100 #orange
	pitems["minecraft:dye",15,random.randint(1, 4)] = 100 #bone meal
	pitems["minecraft:bed",0,random.randint(1, 1)] = 100
	pitems["minecraft:melon",0,random.randint(1, 4)] = 100
	pitems["minecraft:beef",0,random.randint(1, 4)] = 100
	pitems["minecraft:cooked_beef",0,random.randint(1, 2)] = 100
	pitems["minecraft:experience_bottle",0,random.randint(1, 32)] = 500
	pitems["minecraft:carrot",0,random.randint(1, 5)] = 100
	pitems["minecraft:potato",0,random.randint(1, 5)] = 100
	return pitems
	
def oceanChestLoot(options):
	pitems = {}
	pitems["minecraft:air",0,random.randint(1, 1)] = 1900
	pitems["minecraft:sponge",0,random.randint(1, 5)] = 1000
	pitems["minecraft:dye",0,random.randint(1, 4)] = 400  #ink sac
	pitems["minecraft:dye",4,random.randint(1, 4)] = 100  #Lapis
	pitems["minecraft:dye",5,random.randint(1, 4)] = 100  #Purple dye
	pitems["minecraft:dye",6,random.randint(1, 4)] = 100  #Cyan dye
	pitems["minecraft:dye",15,random.randint(1, 4)] = 100 #bone meal
	return pitems
	
def mushroomChestLoot(options):
	pitems = {}
	pitems["minecraft:air",0,random.randint(1, 1)] = 6900
	pitems["minecraft:cooked_beef",0,random.randint(50, 64)] = 50
	pitems["minecraft:cobblestone",0,random.randint(1, 64)] = 100
	pitems["minecraft:sapling",0,random.randint(1, 5)] = 100 #Oak
	pitems["minecraft:sapling",1,random.randint(1, 5)] = 100 #Spruce
	pitems["minecraft:sapling",2,random.randint(1, 5)] = 100 #Birch
	pitems["minecraft:sapling",3,random.randint(1, 5)] = 100 #Jungle
	pitems["minecraft:sapling",4,random.randint(1, 5)] = 100 #Acacia
	pitems["minecraft:sapling",5,random.randint(1, 5)] = 100 #Dark oak
	pitems["minecraft:log",0,random.randint(1, 15)] = 100 #Oak
	pitems["minecraft:log",1,random.randint(1, 15)] = 100 #Spruce
	pitems["minecraft:log",2,random.randint(1, 15)] = 100 #Birch
	pitems["minecraft:log",3,random.randint(1, 15)] = 100 #Jungle
	pitems["minecraft:golden_rail",0,random.randint(1, 10)] = 100
	pitems["minecraft:detector_rail",0,random.randint(1, 10)] = 100
	pitems["minecraft:yellow_flower",0,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",0,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",1,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",2,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",3,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",4,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",5,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",6,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",7,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",8,random.randint(1, 12)] = 100
	pitems["minecraft:ladder",0,random.randint(1, 5)] = 100
	pitems["minecraft:rail",0,random.randint(1, 15)] = 100
	pitems["minecraft:apple",0,random.randint(1, 10)] = 100
	pitems["minecraft:bow",0,random.randint(1, 1)] = 100
	pitems["minecraft:arrow",0,random.randint(1, 12)] = 100
	pitems["minecraft:coal",0,random.randint(1, 6)] = 100
	pitems["minecraft:diamond",0,random.randint(1, 2)] = 50
	pitems["minecraft:iron_ingot",0,random.randint(1, 4)] = 80
	pitems["minecraft:gold_ingot",0,random.randint(1, 2)] = 60
	pitems["minecraft:diamond_sword",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_shovel",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_pickaxe",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_axe",0,random.randint(1, 1)] = 75
	pitems["minecraft:feather",0,random.randint(1, 5)] = 100
	pitems["minecraft:gunpowder",0,random.randint(1, 3)] = 100
	pitems["minecraft:wheat_seeds",0,random.randint(1, 5)] = 100
	pitems["minecraft:wheat",0,random.randint(1, 4)] = 100
	pitems["minecraft:bread",0,random.randint(1, 4)] = 100
	pitems["minecraft:iron_helmet",0,random.randint(1, 1)] = 85
	pitems["minecraft:iron_chestplate",0,random.randint(1, 1)] = 85
	pitems["minecraft:iron_leggings",0,random.randint(1, 1)] = 85
	pitems["minecraft:iron_boots",0,random.randint(1, 1)] = 85
	pitems["minecraft:diamond_helmet",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_chestplate",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_leggings",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_boots",0,random.randint(1, 1)] = 75
	pitems["minecraft:porkchop",0,random.randint(1, 5)] = 100
	pitems["minecraft:cooked_porkchop",0,random.randint(1, 2)] = 100
	pitems["minecraft:golden_apple",0,random.randint(1, 2)] = 25
	pitems["minecraft:golden_apple",1,random.randint(1, 1)] = 25
	pitems["minecraft:water_bucket",0,random.randint(1, 1)] = 100
	pitems["minecraft:lava_bucket",0,random.randint(1, 1)] = 100
	pitems["minecraft:reeds",0,random.randint(1, 5)] = 100
	pitems["minecraft:bed",0,random.randint(1, 1)] = 100
	pitems["minecraft:beef",0,random.randint(1, 4)] = 100
	pitems["minecraft:cooked_beef",0,random.randint(1, 2)] = 100
	pitems["minecraft:chicken",0,random.randint(1, 4)] = 100
	pitems["minecraft:cooked_chicken",0,random.randint(1, 2)] = 100
	pitems["minecraft:ender_pearl",0,random.randint(1, 10)] = 100
	pitems["minecraft:speckled_melon",0,random.randint(1, 3)] = 100
	pitems["minecraft:experience_bottle",0,random.randint(1, 32)] = 500
	pitems["minecraft:carrot",0,random.randint(1, 5)] = 100
	pitems["minecraft:potato",0,random.randint(1, 5)] = 100
	pitems["minecraft:mutton",0,random.randint(1, 5)] = 100
	pitems["minecraft:cooked_mutton",0,random.randint(1, 2)] = 100
	return pitems
	
def mesaChestLoot(options):
	pitems = {}
	pitems["minecraft:air",0,random.randint(1, 1)] = 8000
	pitems["minecraft:cobblestone",0,random.randint(1, 64)] = 100
	pitems["minecraft:sapling",0,random.randint(1, 5)] = 200 #Oak
	pitems["minecraft:sapling",1,random.randint(1, 5)] = 200 #Spruce
	pitems["minecraft:sapling",2,random.randint(1, 5)] = 200 #Birch
	pitems["minecraft:sapling",3,random.randint(1, 5)] = 200 #Jungle
	pitems["minecraft:sapling",4,random.randint(1, 5)] = 200 #Acacia
	pitems["minecraft:sapling",5,random.randint(1, 5)] = 200 #Dark oak
	pitems["minecraft:log",0,random.randint(1, 15)] = 200 #Oak
	pitems["minecraft:log",1,random.randint(1, 15)] = 200 #Spruce
	pitems["minecraft:log",2,random.randint(1, 15)] = 200 #Birch
	pitems["minecraft:log",3,random.randint(1, 15)] = 200 #Jungle
	pitems["minecraft:golden_rail",0,random.randint(1, 10)] = 25
	pitems["minecraft:detector_rail",0,random.randint(1, 10)] = 25
	pitems["minecraft:yellow_flower",0,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",0,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",1,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",2,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",3,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",4,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",5,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",6,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",7,random.randint(1, 12)] = 100
	pitems["minecraft:red_flower",8,random.randint(1, 12)] = 100
	pitems["minecraft:ladder",0,random.randint(1, 5)] = 100
	pitems["minecraft:rail",0,random.randint(1, 15)] = 100
	pitems["minecraft:apple",0,random.randint(1, 10)] = 100
	pitems["minecraft:bow",0,random.randint(1, 1)] = 100
	pitems["minecraft:arrow",0,random.randint(1, 12)] = 100
	pitems["minecraft:coal",0,random.randint(1, 6)] = 100
	pitems["minecraft:diamond",0,random.randint(1, 2)] = 50
	pitems["minecraft:iron_ingot",0,random.randint(1, 4)] = 80
	pitems["minecraft:gold_ingot",0,random.randint(1, 2)] = 65
	pitems["minecraft:diamond_sword",0,random.randint(1, 1)] = 65
	pitems["minecraft:diamond_shovel",0,random.randint(1, 1)] = 65
	pitems["minecraft:diamond_pickaxe",0,random.randint(1, 1)] = 65
	pitems["minecraft:diamond_axe",0,random.randint(1, 1)] = 65
	pitems["minecraft:feather",0,random.randint(1, 5)] = 100
	pitems["minecraft:gunpowder",0,random.randint(1, 3)] = 100
	pitems["minecraft:wheat_seeds",0,random.randint(1, 5)] = 100
	pitems["minecraft:wheat",0,random.randint(1, 4)] = 100
	pitems["minecraft:bread",0,random.randint(1, 4)] = 100
	pitems["minecraft:iron_helmet",0,random.randint(1, 1)] = 75
	pitems["minecraft:iron_chestplate",0,random.randint(1, 1)] = 75
	pitems["minecraft:iron_leggings",0,random.randint(1, 1)] = 75
	pitems["minecraft:iron_boots",0,random.randint(1, 1)] = 75
	pitems["minecraft:diamond_helmet",0,random.randint(1, 1)] = 65
	pitems["minecraft:diamond_chestplate",0,random.randint(1, 1)] = 65
	pitems["minecraft:diamond_leggings",0,random.randint(1, 1)] = 65
	pitems["minecraft:diamond_boots",0,random.randint(1, 1)] = 65
	pitems["minecraft:porkchop",0,random.randint(1, 5)] = 100
	pitems["minecraft:cooked_porkchop",0,random.randint(1, 2)] = 100
	pitems["minecraft:golden_apple",0,random.randint(1, 2)] = 25
	pitems["minecraft:golden_apple",1,random.randint(1, 1)] = 25
	pitems["minecraft:water_bucket",0,random.randint(1, 1)] = 100
	pitems["minecraft:lava_bucket",0,random.randint(1, 1)] = 100
	pitems["minecraft:reeds",0,random.randint(1, 5)] = 100
	pitems["minecraft:dye",1,random.randint(1, 4)] = 100  #rose red
	pitems["minecraft:dye",2,random.randint(1, 4)] = 100  #cactus green
	pitems["minecraft:dye",3,random.randint(1, 4)] = 100  #coco beans
	pitems["minecraft:dye",4,random.randint(1, 4)] = 100  #Lapis
	pitems["minecraft:dye",8,random.randint(1, 4)] = 100  #Gray
	pitems["minecraft:dye",13,random.randint(1, 4)] = 100 #Magenta
	pitems["minecraft:dye",14,random.randint(1, 4)] = 100 #orange
	pitems["minecraft:dye",15,random.randint(1, 4)] = 100 #bone meal
	pitems["minecraft:bed",0,random.randint(1, 1)] = 100
	pitems["minecraft:beef",0,random.randint(1, 4)] = 100
	pitems["minecraft:cooked_beef",0,random.randint(1, 2)] = 100
	pitems["minecraft:chicken",0,random.randint(1, 4)] = 100
	pitems["minecraft:cooked_chicken",0,random.randint(1, 2)] = 100
	pitems["minecraft:ender_pearl",0,random.randint(1, 10)] = 100
	pitems["minecraft:speckled_melon",0,random.randint(1, 3)] = 100
	pitems["minecraft:experience_bottle",0,random.randint(1, 32)] = 400
	pitems["minecraft:carrot",0,random.randint(1, 5)] = 100
	pitems["minecraft:potato",0,random.randint(1, 5)] = 100
	pitems["minecraft:mutton",0,random.randint(1, 5)] = 100
	pitems["minecraft:cooked_mutton",0,random.randint(1, 2)] = 100
	return pitems
	
def overloadedChestLoot(options):
	pitems = {}
	pitems["minecraft:air",0,random.randint(1, 1)] = 99000
	pitems["minecraft:cobblestone",0,random.randint(1, 64)] = 690
	pitems["minecraft:sapling",0,random.randint(1, 5)] = 690 #Oak
	pitems["minecraft:sapling",1,random.randint(1, 5)] = 690 #Spruce
	pitems["minecraft:sapling",2,random.randint(1, 5)] = 690 #Birch
	pitems["minecraft:sapling",3,random.randint(1, 5)] = 690 #Jungle
	pitems["minecraft:sapling",4,random.randint(1, 5)] = 690 #Acacia
	pitems["minecraft:sapling",5,random.randint(1, 5)] = 690 #Dark oak
	pitems["minecraft:log",0,random.randint(1, 15)] = 690 #Oak
	pitems["minecraft:log",1,random.randint(1, 15)] = 690 #Spruce
	pitems["minecraft:log",2,random.randint(1, 15)] = 690 #Birch
	pitems["minecraft:log",3,random.randint(1, 15)] = 690 #Jungle
	pitems["minecraft:golden_rail",0,random.randint(1, 10)] = 690
	pitems["minecraft:detector_rail",0,random.randint(1, 10)] = 690
	pitems["minecraft:yellow_flower",0,random.randint(1, 12)] = 690
	pitems["minecraft:red_flower",0,random.randint(1, 12)] = 690
	pitems["minecraft:red_flower",1,random.randint(1, 12)] = 690
	pitems["minecraft:red_flower",2,random.randint(1, 12)] = 690
	pitems["minecraft:red_flower",3,random.randint(1, 12)] = 690
	pitems["minecraft:red_flower",4,random.randint(1, 12)] = 690
	pitems["minecraft:red_flower",5,random.randint(1, 12)] = 690
	pitems["minecraft:red_flower",6,random.randint(1, 12)] = 690
	pitems["minecraft:red_flower",7,random.randint(1, 12)] = 690
	pitems["minecraft:red_flower",8,random.randint(1, 12)] = 690
	pitems["minecraft:ladder",0,random.randint(1, 5)] = 690
	pitems["minecraft:rail",0,random.randint(1, 15)] = 690
	pitems["minecraft:cactus",0,random.randint(1, 3)] = 690
	pitems["minecraft:vine",0,random.randint(1, 15)] = 690
	pitems["minecraft:waterlily",0,random.randint(1, 4)] = 690
	pitems["minecraft:nether_wart",0,random.randint(1, 5)] = 690
	pitems["minecraft:log2",0,random.randint(1, 5)] = 690 #Acacia
	pitems["minecraft:log2",1,random.randint(1, 5)] = 690 #Dark
	pitems["minecraft:white_shulker_box",0,random.randint(1, 1)] = 690
	pitems["minecraft:orange_shulker_box",0,random.randint(1, 1)] = 690
	pitems["minecraft:magenta_shulker_box",0,random.randint(1, 1)] = 690
	pitems["minecraft:light_blue_shulker_box",0,random.randint(1, 1)] = 690
	pitems["minecraft:yellow_shulker_box",0,random.randint(1, 1)] = 690
	pitems["minecraft:lime_shulker_box",0,random.randint(1, 1)] = 690
	pitems["minecraft:pink_shulker_box",0,random.randint(1, 1)] = 690
	pitems["minecraft:gray_shulker_box",0,random.randint(1, 1)] = 690
	pitems["minecraft:silver_shulker_box",0,random.randint(1, 1)] = 690
	pitems["minecraft:cyan_shulker_box",0,random.randint(1, 1)] = 690
	pitems["minecraft:purple_shulker_box",0,random.randint(1, 1)] = 690
	pitems["minecraft:blue_shulker_box",0,random.randint(1, 1)] = 690
	pitems["minecraft:brown_shulker_box",0,random.randint(1, 1)] = 690
	pitems["minecraft:green_shulker_box",0,random.randint(1, 1)] = 690
	pitems["minecraft:red_shulker_box",0,random.randint(1, 1)] = 690
	pitems["minecraft:black_shulker_box",0,random.randint(1, 1)] = 690
	pitems["minecraft:iron_shovel",0,random.randint(1, 1)] = 690
	pitems["minecraft:iron_pickaxe",0,random.randint(1, 1)] = 690
	pitems["minecraft:iron_axe",0,random.randint(1, 1)] = 690
	pitems["minecraft:flint_and_steel",0,random.randint(1, 1)] = 690
	pitems["minecraft:apple",0,random.randint(1, 10)] = 690
	pitems["minecraft:bow",0,random.randint(1, 1)] = 690
	pitems["minecraft:arrow",0,random.randint(1, 12)] = 690
	pitems["minecraft:coal",0,random.randint(1, 6)] = 690
	pitems["minecraft:diamond",0,random.randint(1, 2)] = 690
	pitems["minecraft:iron_ingot",0,random.randint(1, 4)] = 690
	pitems["minecraft:gold_ingot",0,random.randint(1, 2)] = 690
	pitems["minecraft:iron_sword",0,random.randint(1, 1)] = 690
	pitems["minecraft:diamond_sword",0,random.randint(1, 1)] = 690
	pitems["minecraft:diamond_shovel",0,random.randint(1, 1)] = 690
	pitems["minecraft:diamond_pickaxe",0,random.randint(1, 1)] = 690
	pitems["minecraft:diamond_axe",0,random.randint(1, 1)] = 690
	pitems["minecraft:feather",0,random.randint(1, 5)] = 690
	pitems["minecraft:gunpowder",0,random.randint(1, 3)] = 690
	pitems["minecraft:wheat_seeds",0,random.randint(1, 5)] = 690
	pitems["minecraft:wheat",0,random.randint(1, 4)] = 690
	pitems["minecraft:bread",0,random.randint(1, 4)] = 690
	pitems["minecraft:chainmail_helmet",0,random.randint(1, 1)] = 690
	pitems["minecraft:chainmail_chestplate",0,random.randint(1, 1)] = 690
	pitems["minecraft:chainmail_leggings",0,random.randint(1, 1)] = 690
	pitems["minecraft:chainmail_boots",0,random.randint(1, 1)] = 690
	pitems["minecraft:iron_helmet",0,random.randint(1, 1)] = 690
	pitems["minecraft:iron_chestplate",0,random.randint(1, 1)] = 690
	pitems["minecraft:iron_leggings",0,random.randint(1, 1)] = 690
	pitems["minecraft:iron_boots",0,random.randint(1, 1)] = 690
	pitems["minecraft:diamond_helmet",0,random.randint(1, 1)] = 690
	pitems["minecraft:diamond_chestplate",0,random.randint(1, 1)] = 690
	pitems["minecraft:diamond_leggings",0,random.randint(1, 1)] = 690
	pitems["minecraft:diamond_boots",0,random.randint(1, 1)] = 690
	pitems["minecraft:porkchop",0,random.randint(1, 5)] = 690
	pitems["minecraft:cooked_porkchop",0,random.randint(1, 2)] = 690
	pitems["minecraft:golden_apple",0,random.randint(1, 2)] = 690
	pitems["minecraft:golden_apple",1,random.randint(1, 1)] = 690
	pitems["minecraft:water_bucket",0,random.randint(1, 1)] = 690
	pitems["minecraft:lava_bucket",0,random.randint(1, 1)] = 690
	pitems["minecraft:saddle",0,random.randint(1, 1)] = 690
	pitems["minecraft:leather",0,random.randint(1, 4)] = 690
	pitems["minecraft:reeds",0,random.randint(1, 5)] = 690
	pitems["minecraft:glowstone_dust",0,random.randint(1, 7)] = 690
	pitems["minecraft:dye",0,random.randint(1, 4)] = 690  #ink sac
	pitems["minecraft:dye",1,random.randint(1, 4)] = 690  #rose red
	pitems["minecraft:dye",2,random.randint(1, 4)] = 690  #cactus green
	pitems["minecraft:dye",3,random.randint(1, 4)] = 690  #coco beans
	pitems["minecraft:dye",4,random.randint(1, 4)] = 690  #Lapis
	pitems["minecraft:dye",5,random.randint(1, 4)] = 690  #Purple dye
	pitems["minecraft:dye",6,random.randint(1, 4)] = 690  #Cyan dye
	pitems["minecraft:dye",7,random.randint(1, 4)] = 690  #Light gray
	pitems["minecraft:dye",8,random.randint(1, 4)] = 690  #Gray
	pitems["minecraft:dye",9,random.randint(1, 4)] = 690  #pink
	pitems["minecraft:dye",10,random.randint(1, 4)] = 690 #lime
	pitems["minecraft:dye",11,random.randint(1, 4)] = 690 #dandelion
	pitems["minecraft:dye",12,random.randint(1, 4)] = 690 #Light blue
	pitems["minecraft:dye",13,random.randint(1, 4)] = 690 #Magenta
	pitems["minecraft:dye",14,random.randint(1, 4)] = 690 #orange
	pitems["minecraft:dye",15,random.randint(1, 4)] = 690 #bone meal
	pitems["minecraft:bed",0,random.randint(1, 1)] = 690
	pitems["minecraft:melon",0,random.randint(1, 4)] = 690
	pitems["minecraft:pumpkin_seeds",0,random.randint(1, 3)] = 690
	pitems["minecraft:melon_seeds",0,random.randint(1, 3)] = 690
	pitems["minecraft:beef",0,random.randint(1, 4)] = 690
	pitems["minecraft:cooked_beef",0,random.randint(1, 2)] = 690
	pitems["minecraft:chicken",0,random.randint(1, 4)] = 690
	pitems["minecraft:cooked_chicken",0,random.randint(1, 2)] = 690
	pitems["minecraft:ender_pearl",0,random.randint(1, 10)] = 690
	pitems["minecraft:blaze_rod",0,random.randint(1, 5)] = 690
	pitems["minecraft:ghast_tear",0,random.randint(1, 3)] = 690
	pitems["minecraft:gold_nugget",0,random.randint(1, 15)] = 690
	pitems["minecraft:nether_wart",0,random.randint(1, 4)] = 690
	pitems["minecraft:fermented_spider_eye",0,random.randint(1, 1)] = 690
	pitems["minecraft:magma_cream",0,random.randint(1, 5)] = 690
	pitems["minecraft:ender_eye",0,random.randint(1, 1)] = 690
	pitems["minecraft:speckled_melon",0,random.randint(1, 3)] = 690
	pitems["minecraft:experience_bottle",0,random.randint(1, 32)] = 690
	pitems["minecraft:carrot",0,random.randint(1, 5)] = 690
	pitems["minecraft:potato",0,random.randint(1, 5)] = 690
	pitems["minecraft:golden_carrot",0,random.randint(1, 2)] = 690
	pitems["minecraft:nether_star",0,random.randint(1, 1)] = 690
	pitems["minecraft:iron_horse_armor",0,random.randint(1, 1)] = 690
	pitems["minecraft:golden_horse_armor",0,random.randint(1, 1)] = 690
	pitems["minecraft:diamond_horse_armor",0,random.randint(1, 1)] = 690
	pitems["minecraft:lead",0,random.randint(1, 4)] = 690
	pitems["minecraft:name_tag",0,random.randint(1, 7)] = 690
	pitems["minecraft:mutton",0,random.randint(1, 5)] = 690
	pitems["minecraft:cooked_mutton",0,random.randint(1, 2)] = 690
	pitems["minecraft:chorus_fruit",0,random.randint(1, 6)] = 690
	pitems["minecraft:popped_chorus_fruit",0,random.randint(1, 15)] = 690
	pitems["minecraft:beetroot",0,random.randint(1, 2)] = 690
	pitems["minecraft:dragon_breath",0,random.randint(1, 5)] = 690
	pitems["minecraft:spectral_arrow",0,random.randint(4, 8)] = 690
	pitems["minecraft:tipped_arrow",0,random.randint(4, 10)] = 690
	pitems["minecraft:elytra",0,random.randint(1, 1)] = 690
	pitems["minecraft:totem_of_undying",0,random.randint(1, 1)] = 690
	return pitems
	
	
# Block distributions
def overworldp(options):
	spawnchanceSpawner = options["Spawner probability (Lower = rare):"]
	spawnchanceChest = options["Chest probability (Lower = rare):"]
	spawners = options["Enable spawners"]
	chests = options["Enable chests"]
	#p[blockid,dataid] = prob.
	p = {}
	p[1,0] = 60000   #Stone
	p[1,1] = 5000    #Granite
	p[1,3] = 5000    #Diorite
	p[1,5] = 5000    #Andesite
	p[2,0] = 5000    #Grass
	p[3,0] = 17000   #Dirt
	p[3,2] = 500     #Podzol
	p[5,0] = 500     #Oak Planks
	p[5,1] = 500     #Spruce Planks
	p[5,2] = 500     #Birch Planks
	p[5,3] = 500     #Jungle Planks
	p[5,4] = 500     #Acacia Planks
	p[5,5] = 500     #Dark oak Planks
	p[9,0] = 500     #Still Water
	p[11,0] = 500    #Still Lava
	p[12,0] = 1000   #Sand
	p[12,0] = 500    #Red Sand
	p[13,0] = 1000   #Gravel
	p[14,0] = 900    #Gold Ore
	p[15,0] = 3500   #Iron Ore
	p[16,0] = 4000   #Coal Ore
	p[17,0] = 4000   #Oak wood
	p[17,1] = 4000   #Spruce wood
	p[17,2] = 4000   #Birch wood
	p[17,3] = 4000   #Jungle wood
	p[18,0] = 200    #Oak leaves
	p[18,1] = 200    #Spruce leaves
	p[18,2] = 200    #Birch leaves
	p[18,3] = 200    #Jungle leaves
	p[19,1] = 30     #Wet sponge
	p[20,0] = 20     #Glass
	p[21,0] = 1600   #Lapis ore
	p[24,0] = 1000   #Sandstone
	p[29,0] = 500    #Sticky piston
	p[30,0] = 500    #Cobwebs
	p[33,0] = 500    #Piston
	p[35,0] = 500    #White wool
	p[35,4] = 500    #Yellow wool
	p[35,3] = 500    #Blue wool
	p[35,14] = 500   #Red wool
	p[46,0] = 500    #TNT
	p[47,0] = 500    #Bookshelf
	p[48,0] = 500    #Moss stone
	p[49,0] = 500    #Obsidian
	p[56,0] = 300    #Diamond ore
	p[73,0] = 2300   #Redstone ore
	p[79,0] = 500    #Ice
	p[82,0] = 1000   #Clay
	p[86,0] = 500    #Pumpkin
	p[99,14] = 500   #Brown mushroom
	p[100,14] = 500  #Red mushroom
	p[103,0] = 500   #Melon Block
	p[110,0] = 500   #Mycelium
	p[116,0] = 20    #Enchantment table
	p[129,0] = 100   #Emerald ore
	p[159,0] = 500   #White Stained clay
	p[159,1] = 500   #Orage Stained clay
	p[159,2] = 500   #Magenta Stained clay
	p[159,3] = 500   #Light Blue Stained clay
	p[159,4] = 500   #Yellow Stained clay
	p[159,5] = 500   #Lime Stained clay
	p[159,6] = 500   #Pink Stained clay
	p[159,7] = 500   #Gray Stained clay
	p[159,8] = 500   #Light gray Stained clay
	p[159,9] = 500   #Cyan Stained clay
	p[159,10] = 500  #Purple Stained clay
	p[159,11] = 500  #Blue Stained clay
	p[159,12] = 500  #Brown Stained clay
	p[159,13] = 500  #Green Stained clay
	p[159,14] = 500  #Red Stained clay
	p[159,15] = 500  #Black Stained clay
	p[161,0] = 50    #Acacia Leaves
	p[161,1] = 50    #Dark oak leaves
	p[162,0] = 4000  #Acacia wood
	p[162,1] = 4000  #Dark oak wood
	p[165,0] = 50    #Slime block
	p[168,0] = 2000  #Prismarine
	p[168,2] = 1000  #Dark Prismarine
	p[169,0] = 400   #Sea Lantern
	p[170,0] = 250   #Hay Bale
	p[174,0] = 1000  #Packed Ice
	p[179,0] = 1000  #Red Sandstone
	if options["Game version"] == "1.12+":
		p[251,0] = 50  #concrete
		p[251,1] = 50  #concrete
		p[251,2] = 50  #concrete
		p[251,3] = 50  #concrete
		p[251,4] = 50  #concrete
		p[251,5] = 50  #concrete
		p[251,6] = 50  #concrete
		p[251,7] = 50  #concrete
		p[251,8] = 50  #concrete
		p[251,9] = 50  #concrete
		p[251,10] = 50 #concrete
		p[251,11] = 50 #concrete
		p[251,12] = 50 #concrete
		p[251,13] = 50 #concrete
		p[251,14] = 50 #concrete
		p[251,15] = 50 #concrete
		p[252,0] = 25  #concrete powder
		p[252,1] = 25  #concrete powder
		p[252,2] = 25  #concrete powder
		p[252,3] = 25  #concrete powder
		p[252,4] = 25  #concrete powder
		p[252,5] = 25  #concrete powder
		p[252,6] = 25  #concrete powder
		p[252,7] = 25  #concrete powder
		p[252,8] = 25  #concrete powder
		p[252,9] = 25  #concrete powder
		p[252,10] = 25 #concrete powder
		p[252,11] = 25 #concrete powder
		p[252,12] = 25 #concrete powder
		p[252,13] = 25 #concrete powder
		p[252,14] = 25 #concrete powder
		p[252,15] = 25 #concrete powder
		p[235,1] = 7   #glazed terracotta
		p[236,1] = 7   #glazed terracotta
		p[237,1] = 7   #glazed terracotta
		p[238,1] = 7   #glazed terracotta
		p[239,1] = 7   #glazed terracotta
		p[240,1] = 7   #glazed terracotta
		p[241,1] = 7   #glazed terracotta
		p[242,1] = 7   #glazed terracotta
		p[243,1] = 7   #glazed terracotta
		p[245,1] = 7   #glazed terracotta
		p[246,1] = 7   #glazed terracotta
		p[247,1] = 7   #glazed terracotta
		p[248,1] = 7   #glazed terracotta
		p[249,1] = 7   #glazed terracotta
		p[250,1] = 7   #glazed terracotta
		
	if chests:
		p[54,3] = spawnchanceChest
	if spawners:
		p[52,0] = spawnchanceSpawner
	return p
	
def netherp(options):
	spawnchanceSpawner = options["Spawner probability (Lower = rare):"]
	spawnchanceChest = options["Chest probability (Lower = rare):"]
	spawners = options["Enable spawners"]
	chests = options["Enable chests"]
	p = {}
	p[11,0] = 25000 #Lava
	p[14,0] = 2000  #Gold Ore
	p[41,0] = 800   #Gold block
	p[87,0] = 38000 #Netherrack
	p[88,0] = 7000  #Soul Sand
	p[89,0] = 5000  #Glowstone
	p[112,0] = 5000 #Nether Brick
	p[153,0] = 7000 #Nether quartz ore
	p[213,0] = 8000 #Magma block
	p[215,0] = 2000 #Red Nether Brick
	p[216,0] = 1000 #Bone Block
	
	if chests:
		p[54,3] = spawnchanceChest
	if spawners:
		p[52,0] = spawnchanceSpawner
	return p
	
def endp(options):
	spawnchanceSpawner = options["Spawner probability (Lower = rare):"]
	spawnchanceChest = options["Chest probability (Lower = rare):"]
	spawners = options["Enable spawners"]
	chests = options["Enable chests"]
	p = {}
	p[9,0] = 1000    #water
	p[47,0] = 500    #bookshelf
	p[49,0] = 25000  #obsidian
	p[98,1] = 2000	 #mossy stone bricks
	p[98,0] = 3000	 #stone bricks
	p[101,0] = 2000	 #iron bar
	p[121,0] = 60000 #end stone
	p[133,0] = 150	 #emerald block
	p[138,0] = 5	 #beacon
	p[206,0] = 20000 #End stone bricks
	
	if chests:
		p[54,3] = spawnchanceChest #Chest
	if spawners:
		p[52,0] = spawnchanceSpawner #spawner
	return p
	
def normalp(options):
	spawnchanceSpawner = options["Spawner probability (Lower = rare):"]
	spawnchanceChest = options["Chest probability (Lower = rare):"]
	spawners = options["Enable spawners"]
	chests = options["Enable chests"]
	p = {}
	p[1,0] = 50000  #Stone
	p[1,1] = 2000   #Granite
	p[1,3] = 2000   #Diorite
	p[1,5] = 2000   #Andesite
	p[2,0] = 1000   #Grass
	p[3,0] = 7000   #Dirt
	p[5,0] = 1000   #Oak Planks
	p[5,1] = 1000   #Spruce Planks
	p[5,2] = 1000   #Birch Planks
	p[5,5] = 1000   #Dark oak Planks
	p[9,0] = 100    #Still Water
	p[11,0] = 100   #Still Lava
	p[13,0] = 4000  #Gravel
	p[14,0] = 900   #Gold Ore
	p[15,0] = 5100  #Iron Ore
	p[16,0] = 5800  #Coal Ore
	p[17,0] = 500   #Oak wood
	p[17,1] = 500   #Spruce wood
	p[17,2] = 500   #Birch wood
	p[18,0] = 100   #Oak leaves
	p[18,1] = 100   #Spruce leaves
	p[18,2] = 100   #Birch leaves
	p[20,0] = 100   #Glass
	p[21,0] = 1600  #Lapis ore
	p[29,0] = 400   #Sticky piston
	p[30,0] = 50    #Cobwebs
	p[33,0] = 400   #Piston
	p[35,0] = 100   #White wool
	p[35,4] = 100   #Yellow wool
	p[35,3] = 100   #Blue wool
	p[35,14] = 100  #Red wool
	p[49,0] = 1000  #Obsidian
	p[56,0] = 300   #Diamond ore
	p[73,0] = 2300  #Redstone ore
	p[129,0] = 100  #Emerald ore
	p[161,1] = 500  #Dark oak leaves
	p[162,1] = 500  #Dark oak wood
	if options["Game version"] == "1.12+":
		p[251,0] = 25  #concrete
		p[251,1] = 25  #concrete
		p[251,2] = 25  #concrete
		p[251,3] = 25  #concrete
		p[251,4] = 25  #concrete
		p[251,5] = 25  #concrete
		p[251,6] = 25  #concrete
		p[251,7] = 25  #concrete
		p[251,8] = 25  #concrete
		p[251,9] = 25  #concrete
		p[251,10] = 25 #concrete
		p[251,11] = 25 #concrete
		p[251,12] = 25 #concrete
		p[251,13] = 25 #concrete
		p[251,14] = 25 #concrete
		p[251,15] = 25 #concrete
		p[252,0] = 25  #concrete powder
		p[252,1] = 25  #concrete powder
		p[252,2] = 25  #concrete powder
		p[252,3] = 25  #concrete powder
		p[252,4] = 25  #concrete powder
		p[252,5] = 25  #concrete powder
		p[252,6] = 25  #concrete powder
		p[252,7] = 25  #concrete powder
		p[252,8] = 25  #concrete powder
		p[252,9] = 25  #concrete powder
		p[252,10] = 25 #concrete powder
		p[252,11] = 25 #concrete powder
		p[252,12] = 25 #concrete powder
		p[252,13] = 25 #concrete powder
		p[252,14] = 25 #concrete powder
		p[252,15] = 25 #concrete powder
		p[235,1] = 7   #glazed terracotta
		p[236,1] = 7   #glazed terracotta
		p[237,1] = 7   #glazed terracotta
		p[238,1] = 7   #glazed terracotta
		p[239,1] = 7   #glazed terracotta
		p[240,1] = 7   #glazed terracotta
		p[241,1] = 7   #glazed terracotta
		p[242,1] = 7   #glazed terracotta
		p[243,1] = 7   #glazed terracotta
		p[244,1] = 7   #glazed terracotta
		p[245,1] = 7   #glazed terracotta
		p[246,1] = 7   #glazed terracotta
		p[247,1] = 7   #glazed terracotta
		p[248,1] = 7   #glazed terracotta
		p[249,1] = 7   #glazed terracotta
		p[250,1] = 7   #glazed terracotta	

	if chests:
		p[54,3] = spawnchanceChest #Chest
	if spawners:
		p[52,0] = spawnchanceSpawner #spawner
	return p
	
def icep(options):
	spawnchanceSpawner = options["Spawner probability (Lower = rare):"]
	spawnchanceChest = options["Chest probability (Lower = rare):"]
	spawners = options["Enable spawners"]
	chests = options["Enable chests"]
	p = {}
	p[1,0] = 9000    #Stone
	p[14,0] = 900    #Gold Ore
	p[15,0] = 5100   #Iron Ore
	p[16,0] = 5800   #Coal ore
	p[21,0] = 1600   #Lapis ore
	p[42,0] = 100    #Iron Block
	p[56,0] = 300    #Diamond ore
	p[80,0] = 15000  #Snow block
	p[73,0] = 2300   #Redstone ore
	p[79,0] = 29000  #Ice
	p[129,0] = 100   #Emerald ore
	p[174,0] = 29000 #Packed Ice
	
	if chests:
		p[54,3] = spawnchanceChest #Chest
	if spawners:
		p[52,0] = spawnchanceSpawner #spawner
	return p
	
def junglep(options):
	spawnchanceSpawner = options["Spawner probability (Lower = rare):"]
	spawnchanceChest = options["Chest probability (Lower = rare):"]
	spawners = options["Enable spawners"]
	chests = options["Enable chests"]
	p = {}
	p[1,0] = 4500   #Stone
	p[2,0] = 1500   #Grass
	p[3,0] = 4500   #Drit
	p[3,1] = 1500   #Coarse Dirt
	p[3,2] = 2500   #Podzol
	p[4,0] = 2000   #Cobblestone
	p[9,0] = 800    #Water
	p[14,0] = 1400  #Gold Ore
	p[15,0] = 5600  #Iron Ore
	p[16,0] = 6300  #Coal ore
	p[21,0] = 2100  #Lapis ore
	p[17,3] = 35500 #Jungle wood
	p[18,3] = 17500 #Jungle leaves
	p[29,0] = 800   #Sticky piston
	p[33,0] = 800   #Piston
	p[48,0] = 2500  #Moss stone
	p[56,0] = 400   #Diamond ore
	p[73,0] = 2800  #Redstone ore
	p[86,0] = 1500  #Pumbkin
	p[98,1] = 2500  #Mossy stone bricks
	p[103,0] = 1500 #Melon block
	p[129,0] = 650  #Emerald ore
	p[132,0] = 1500 #String
	if options["Game version"] == "1.12+":
		p[235,1] = 30  #glazed terracotta
		p[236,1] = 30  #glazed terracotta
		p[237,1] = 30  #glazed terracotta
		p[238,1] = 30  #glazed terracotta
		p[239,1] = 30  #glazed terracotta
		p[240,1] = 30  #glazed terracotta
		p[241,1] = 30  #glazed terracotta
		p[242,1] = 30  #glazed terracotta
		p[243,1] = 30  #glazed terracotta
		p[244,1] = 30  #glazed terracotta
		p[245,1] = 30  #glazed terracotta
		p[246,1] = 30  #glazed terracotta
		p[247,1] = 30  #glazed terracotta
		p[248,1] = 30  #glazed terracotta
		p[249,1] = 30  #glazed terracotta
		p[250,1] = 30  #glazed terracotta	
	
	if chests:
		p[54,3] = spawnchanceChest #Chest
	if spawners:
		p[52,0] = spawnchanceSpawner #spawner
	return p

def swampp(options):
	spawnchanceSpawner = options["Spawner probability (Lower = rare):"]
	spawnchanceChest = options["Chest probability (Lower = rare):"]
	spawners = options["Enable spawners"]
	chests = options["Enable chests"]
	p = {}
	p[1,0] = 3000   #Stone
	p[2,0] = 1000   #Grass
	p[5,0] = 4000   #Oak wood plank
	p[9,0] = 6000   #Water
	p[12,0] = 3000  #Sand
	p[13,0] = 7000  #Gravel
	p[14,0] = 900   #Gold Ore
	p[15,0] = 5100  #Iron Ore
	p[16,0] = 5800  #Coal ore
	p[17,0] = 8000  #Oak wood
	p[18,0] = 1000  #Oak leaves
	p[21,0] = 1600  #Lapis ore
	p[47,0] = 100   #Bookshelf
	p[56,0] = 300   #Diamond ore
	p[73,0] = 2300  #Redstone ore
	p[82,0] = 2000  #Clay
	p[129,0] = 100  #Emerald ore
	p[165,0] = 5000 #Slime block
	p[208,0] = 1500 #Grass path
	
	
	if chests:
		p[54,3] = spawnchanceChest #Chest
	if spawners:
		p[52,0] = spawnchanceSpawner #spawner
	return p

def desertp(options):
	spawnchanceSpawner = options["Spawner probability (Lower = rare):"]
	spawnchanceChest = options["Chest probability (Lower = rare):"]
	spawners = options["Enable spawners"]
	chests = options["Enable chests"]
	p = {}
	p[1,0] = 5500    #Stone
	p[5,3] = 5500    #Acacia wood plank
	p[12,0] = 19900  #sand
	p[12,1] = 12500  #Red sand
	p[14,0] = 1400   #Gold Ore
	p[15,0] = 5600   #Iron Ore
	p[16,0] = 6300   #Coal ore
	p[21,0] = 2100   #Lapis ore
	p[24,0] = 25500  #Sandstone
	p[56,0] = 800    #Diamond ore
	p[73,0] = 2800   #Redstone ore
	p[92,0] = 550    #Cake block
	p[129,0] = 650   #Emerald ore
	p[162,0] = 6500  #Acacia wood
	p[172,0] = 1500  #Hardened clay
	p[179,0] = 2500  #Red sandstone
	p[208,0] = 1500  #Grass path
	
	
	if chests:
		p[54,3] = spawnchanceChest #Chest
	if spawners:
		p[52,0] = spawnchanceSpawner #spawner
	return p

def oceanp(options):
	spawnchanceSpawner = options["Spawner probability (Lower = rare):"]
	spawnchanceChest = options["Chest probability (Lower = rare):"]
	spawners = options["Enable spawners"]
	chests = options["Enable chests"]
	p = {}
	p[1,0] = 15000    #Stone
	p[9,0] = 50000    #Water
	p[12,0] = 5000    #Sand
	p[13,0] = 5000    #Gravel
	p[14,0] = 900     #Gold Ore
	p[15,0] = 5100    #Iron Ore
	p[16,0] = 5800    #Coal ore
	p[19,1] = 200     #Wet Sponge
	p[21,0] = 1600    #Lapis ore
	p[56,0] = 300     #Diamond ore
	p[73,0] = 2300    #Redstone ore
	p[82,0] = 2000    #Clay
	p[129,0] = 150    #Emerald ore
	p[168,0] = 2500   #Prismarine
	p[168,2] = 2500   #Dark Prismarine
	p[169,0] = 500    #Sea Lantern

	if chests:
		p[54,3] = spawnchanceChest #Chest
	if spawners:
		p[52,0] = spawnchanceSpawner #spawner
	return p

def mushroomp(options):
	spawnchanceSpawner = options["Spawner probability (Lower = rare):"]
	spawnchanceChest = options["Chest probability (Lower = rare):"]
	spawners = options["Enable spawners"]
	chests = options["Enable chests"]
	p = {}
	p[1,0] = 16800    #Stone
	p[14,0] = 900     #Gold Ore
	p[15,0] = 5100    #Iron Ore
	p[16,0] = 5800    #Coal ore
	p[21,0] = 1600    #Lapis ore
	p[56,0] = 300     #Diamond ore
	p[73,0] = 2300    #Redstone ore
	p[99,14] = 12600  #Brown mushroom
	p[100,14] = 12600 #Red mushroom
	p[110,0] = 42000  #Mycelium
	
	if chests:
		p[54,3] = spawnchanceChest #Chest
	if spawners:
		p[52,0] = spawnchanceSpawner #spawner
	return p

def mesap(options):
	spawnchanceSpawner = options["Spawner probability (Lower = rare):"]
	spawnchanceChest = options["Chest probability (Lower = rare):"]
	spawners = options["Enable spawners"]
	chests = options["Enable chests"]
	p = {}
	#50000
	p[14,0] = 900     #Gold Ore
	p[15,0] = 5100    #Iron Ore
	p[16,0] = 5800    #Coal ore
	p[21,0] = 1600    #Lapis ore
	p[56,0] = 300     #Diamond ore
	p[73,0] = 2300    #Redstone ore
	p[159,0] = 4941   #White Stained clay
	p[159,1] = 4941   #Orage Stained clay
	p[159,2] = 4941   #Magenta Stained clay
	p[159,3] = 4941   #Light Blue Stained clay
	p[159,4] = 4941   #Yellow Stained clay
	p[159,5] = 4941   #Lime Stained clay
	p[159,6] = 4941   #Pink Stained clay
	p[159,7] = 4941   #Gray Stained clay
	p[159,8] = 4941   #Light gray Stained clay
	p[159,9] = 4941   #Cyan Stained clay
	p[159,10] = 4941  #Purple Stained clay
	p[159,11] = 4941  #Blue Stained clay
	p[159,12] = 4944  #Brown Stained clay
	p[159,13] = 4941  #Green Stained clay
	p[159,14] = 4941  #Red Stained clay
	p[159,15] = 4941  #Black Stained clay
	p[172,0] = 4941   #Hardened clay
	if options["Game version"] == "1.12+":
		p[251,0] = 200   #concrete
		p[251,1] = 200   #concrete
		p[251,2] = 200   #concrete
		p[251,3] = 200   #concrete
		p[251,4] = 200   #concrete
		p[251,5] = 200   #concrete
		p[251,6] = 200   #concrete
		p[251,7] = 200   #concrete
		p[251,8] = 200   #concrete
		p[251,9] = 200   #concrete
		p[251,10] = 200  #concrete
		p[251,11] = 200  #concrete
		p[251,12] = 200  #concrete
		p[251,13] = 200  #concrete
		p[251,14] = 200  #concrete
		p[251,15] = 200  #concrete
		p[252,0] = 200   #concrete powder
		p[252,1] = 200   #concrete powder
		p[252,2] = 200   #concrete powder
		p[252,3] = 200   #concrete powder
		p[252,4] = 200   #concrete powder
		p[252,5] = 200   #concrete powder
		p[252,6] = 200   #concrete powder
		p[252,7] = 200   #concrete powder
		p[252,8] = 200   #concrete powder
		p[252,9] = 200   #concrete powder
		p[252,10] = 200  #concrete powder
		p[252,11] = 200  #concrete powder
		p[252,12] = 200  #concrete powder
		p[252,13] = 200  #concrete powder
		p[252,14] = 200  #concrete powder
		p[252,15] = 200  #concrete powder
		p[235,1] = 100   #glazed terracotta
		p[236,1] = 100   #glazed terracotta
		p[237,1] = 100   #glazed terracotta
		p[238,1] = 100   #glazed terracotta
		p[239,1] = 100   #glazed terracotta
		p[240,1] = 100   #glazed terracotta
		p[241,1] = 100   #glazed terracotta
		p[242,1] = 100   #glazed terracotta
		p[243,1] = 100   #glazed terracotta
		p[244,1] = 100   #glazed terracotta
		p[245,1] = 100   #glazed terracotta
		p[246,1] = 100   #glazed terracotta
		p[247,1] = 100   #glazed terracotta
		p[248,1] = 100   #glazed terracotta
		p[249,1] = 100   #glazed terracotta
		p[250,1] = 100   #glazed terracotta		
	
	if chests:
		p[54,3] = spawnchanceChest #Chest
	if spawners:
		p[52,0] = spawnchanceSpawner #spawner
	return p

def overloadedp(options):
	spawnchanceSpawner = options["Spawner probability (Lower = rare):"]
	spawnchanceChest = options["Chest probability (Lower = rare):"]
	spawners = options["Enable spawners"]
	chests = options["Enable chests"]
	p = {}
	p[1,0] = 500    #Stone
	p[1,1] = 398    #Granite
	p[1,2] = 398    #Polished Granite
	p[1,3] = 398    #Diorite
	p[1,4] = 398    #Polished Diorite
	p[1,5] = 398    #Andesite
	p[1,6] = 398    #Polished Andesite
	p[2,0] = 398    #Grass
	p[3,0] = 398    #Dirt
	p[3,1] = 398    #Coarse dirt
	p[3,2] = 398    #Podzol
	p[4,0] = 398    #Cobblestone
	p[5,0] = 398    #Oak Planks
	p[5,1] = 398    #Spruce Planks
	p[5,2] = 398    #Birch Planks
	p[5,3] = 398    #Jungle Planks
	p[5,4] = 398    #Acacia Planks
	p[5,5] = 398    #Dark oak Planks
	p[7,0] = 398    #Bedrock
	p[9,0] = 398    #Still Water
	p[11,0] = 398   #Still Lava
	p[12,0] = 398   #Sand
	p[12,0] = 398   #Red Sand
	p[13,0] = 398   #Gravel
	p[14,0] = 398   #Gold Ore
	p[15,0] = 398   #Iron Ore
	p[16,0] = 398   #Coal Ore
	p[17,0] = 398   #Oak wood
	p[17,1] = 398   #Spruce wood
	p[17,2] = 398   #Birch wood
	p[17,3] = 398   #Jungle wood
	p[18,0] = 398   #Oak leaves
	p[18,1] = 398   #Spruce leaves
	p[18,2] = 398   #Birch leaves
	p[18,3] = 398   #Jungle leaves
	p[19,0] = 398   #Sponge
	p[19,1] = 398   #Wet sponge
	p[20,0] = 398   #Glass
	p[21,0] = 398   #Lapis ore
	p[22,0] = 398   #Lapis block
	p[23,0] = 398   #Dispenser
	p[24,0] = 398   #Sandstone
	p[24,1] = 398   #Chiseled sandstone
	p[24,2] = 398   #Smooth sandstone
	p[25,0] = 398   #Noteblock
	p[29,0] = 398   #Sticky piston
	p[30,0] = 398   #Cobweb
	p[33,0] = 398   #Piston
	p[35,0] = 398   #White wool
	p[35,1] = 398   #Oragne wool
	p[35,2] = 398   #Magenta wool
	p[35,3] = 398   #Light Blue wool
	p[35,4] = 398   #Yellow wool
	p[35,5] = 398   #Lime green wool
	p[35,6] = 398   #Pink wool
	p[35,7] = 398   #Gray wool
	p[35,8] = 398   #Light gray wool
	p[35,9] = 398   #Cyan wool
	p[35,10] = 398  #Purple wool
	p[35,11] = 398  #Blue wool
	p[35,12] = 398  #Brown wool
	p[35,13] = 398  #Green wool
	p[35,14] = 398  #Red wool
	p[35,15] = 398  #Black wool
	p[41,0] = 398   #Gold block
	p[42,0] = 398   #Iron block
	p[43,0] = 398   #double slab stone
	p[43,1] = 398   #double slab sandstone
	p[43,2] = 398   #double slab Wood
	p[43,3] = 398   #double slab cobble
	p[43,4] = 398   #double slab brick
	p[43,5] = 398   #double slab bricks
	p[43,6] = 398   #double slab nether brick
	p[43,7] = 398   #double slab quartz
	p[44,0] = 398   #slab stone
	p[44,1] = 398   #slab sandstone
	p[44,2] = 398   #slab Wood
	p[44,3] = 398   #slab cobble
	p[44,4] = 398   #slab brick
	p[44,5] = 398   #slab bricks
	p[44,6] = 398   #slab nether brick
	p[44,7] = 398   #slab quartz
	p[45,0] = 398   #Bricks
	p[46,0] = 398   #TNT
	p[47,0] = 398   #Bookshelf
	p[48,0] = 398   #Moss stone
	p[49,0] = 398   #Obsidian
	p[53,0] = 398   #Oak wood stair
	p[56,0] = 398   #Diamond ore
	p[57,0] = 398   #Diamond block
	p[58,0] = 398   #Crafting table
	p[60,0] = 398   #Farm land
	p[61,0] = 398   #Furnace
	p[67,0] = 398   #Cobblestone stairs
	p[73,0] = 398   #Redstone ore
	p[79,0] = 398   #Ice
	p[80,0] = 398   #Snow block
	p[82,0] = 398   #Clay
	p[84,0] = 398   #Jukebox
	p[85,0] = 398   #Fence
	p[86,0] = 398   #Pumpkin
	p[87,0] = 398   #Netherrack
	p[88,0] = 398   #Soul sand
	p[89,0] = 398   #Glow stone
	p[91,0] = 398   #Jack O Lantern
	p[92,0] = 398   #Cake block
	p[95,0] = 398   #White Stained Glass
	p[95,1] = 398   #Orange Stained Glass
	p[95,2] = 398   #Magenta Stained Glass
	p[95,3] = 398   #Light Blue Stained Glass
	p[95,4] = 398   #Yellow Stained Glass
	p[95,5] = 398   #Lime green Stained Glass
	p[95,6] = 398   #Pink Stained Glass
	p[95,7] = 398   #Gray Stained Glass
	p[95,8] = 398   #Light gray Stained Glass
	p[95,9] = 398   #Cyan Stained Glass
	p[95,10] = 398  #Purple Stained Glass
	p[95,11] = 398  #Blue Stained Glass
	p[95,12] = 398  #Brown Stained Glass
	p[95,13] = 398  #Green Stained Glass
	p[95,14] = 398  #Red Stained Glass
	p[95,15] = 398  #Black Stained Glass
	p[96,0] = 398   #Trap door
	p[98,0] = 398   #Stone brick
	p[98,1] = 398   #Mossy brick
	p[98,2] = 398   #Cracked brick
	p[98,3] = 398   #Chiseled brick
	p[99,14] = 398  #Brown mushroom
	p[100,14] = 398 #Red mushroom
	p[101,0] = 398  #Iron bar
	p[102,0] = 398  #Glass pane
	p[103,0] = 398  #Melon block
	p[107,0] = 398  #Oak fence
	p[108,0] = 398  #Brick stairs
	p[109,0] = 398  #Stone stairs
	p[110,0] = 398  #Mycelium
	p[112,0] = 398  #Nether brick
	p[113,0] = 398  #Nether brick
	p[114,0] = 398  #Nether brick stairs
	p[116,0] = 398  #Enchantment table
	p[117,0] = 398  #Brewing stand
	p[118,0] = 398  #Cauldron
	p[121,0] = 398  #End stone
	p[123,0] = 398  #Redstone lamp
	p[125,0] = 398  #Oak Wood double slab
	p[125,1] = 398  #Spruce Wood double slab
	p[125,2] = 398  #Birch Wood double slab
	p[125,3] = 398  #Jungle Wood double slab
	p[125,4] = 398  #Acacia Wood double slab
	p[125,5] = 398  #Dark Wood double slab
	p[126,0] = 398  #Oak Wood slab
	p[126,1] = 398  #Spruce Wood slab
	p[126,2] = 398  #Birch Wood slab
	p[126,3] = 398  #Jungle Wood slab
	p[126,4] = 398  #Acacia Wood slab
	p[126,5] = 398  #Dark Wood slab
	p[128,0] = 398  #Sandstone stairs
	p[129,0] = 398  #Emerald ore
	p[133,0] = 398  #Emerald block
	p[134,0] = 398  #Spruce stairs
	p[135,0] = 398  #Birch stairs
	p[136,0] = 398  #Jungle stairs
	p[138,0] = 398  #Beacon
	p[139,0] = 398  #Cobblestone wall
	p[139,1] = 398  #Mossy cobblestone wall
	p[140,0] = 398  #Flower pot
	p[152,0] = 398  #Redstone block
	p[153,0] = 398  #Nether quartz ore
	p[155,0] = 398  #Quartz block
	p[155,1] = 398  #Chiseled quartz
	p[155,2] = 398  #pillar quartz
	p[156,0] = 398  #Quartz stairs
	p[159,0] = 398  #White Stained clay
	p[159,1] = 398  #Orage Stained clay
	p[159,2] = 398  #Magenta Stained clay
	p[159,3] = 398  #Light Blue Stained clay
	p[159,4] = 398  #Yellow Stained clay
	p[159,5] = 398  #Lime Stained clay
	p[159,6] = 398  #Pink Stained clay
	p[159,7] = 398  #Gray Stained clay
	p[159,8] = 398  #Light gray Stained clay
	p[159,9] = 398  #Cyan Stained clay
	p[159,10] = 398 #Purple Stained clay
	p[159,11] = 398 #Blue Stained clay
	p[159,12] = 398 #Brown Stained clay
	p[159,13] = 398 #Green Stained clay
	p[159,14] = 398 #Red Stained clay
	p[159,15] = 398 #Black Stained clay
	p[160,0] = 398  #White stained glass pane
	p[160,1] = 398  #Orage stained glass pane
	p[160,2] = 398  #Magenta stained glass pane
	p[160,3] = 398  #Light Blue stained glass pane
	p[160,4] = 398  #Yellow stained glass pane
	p[160,5] = 398  #Lime stained glass pane
	p[160,6] = 398  #Pink stained glass pane
	p[160,7] = 398  #Gray stained glass pane
	p[160,8] = 398  #Light gray stained glass pane
	p[160,9] = 398  #Cyan stained glass pane
	p[160,10] = 398 #Purple stained glass pane
	p[160,11] = 398 #Blue stained glass pane
	p[160,12] = 398 #Brown stained glass pane
	p[160,13] = 398 #Green stained glass pane
	p[160,14] = 398 #Red stained glass pane
	p[160,15] = 398 #Black stained glass pane
	p[161,0] = 398  #Acacia Leaves
	p[161,1] = 398  #Dark oak leaves
	p[162,0] = 398  #Acacia wood
	p[162,1] = 398  #Dark oak wood
	p[163,0] = 398  #Acacia wood stair
	p[164,0] = 398  #Dark oak stair
	p[165,0] = 398  #Slime block
	p[166,0] = 398  #Barrier block
	p[167,0] = 398  #Iron trap door
	p[168,0] = 398  #Prismarine
	p[168,1] = 398  #Prismarine bricks
	p[168,2] = 398  #Dark Prismarine
	p[169,0] = 398  #Sea Lantern
	p[170,0] = 398  #Hay Bale
	p[172,0] = 398  #Hardened clay
	p[173,0] = 398  #Block of coal
	p[174,0] = 398  #Packed Ice
	p[179,0] = 398  #Red Sandstone
	p[179,1] = 398  #Chiseled red sandstone
	p[179,2] = 398  #Smooth red sandstone
	p[180,0] = 398  #Red sandstone stairs
	p[182,0] = 398  #Red sandstone slab
	p[183,0] = 398  #Spruce gate
	p[184,0] = 398  #Birch gate
	p[185,0] = 398  #Jungle gate
	p[186,0] = 398  #Dark gate
	p[187,0] = 398  #Acacia gate
	p[188,0] = 398  #Spruce fence
	p[189,0] = 398  #Birch fence
	p[190,0] = 398  #Jungle fence
	p[191,0] = 398  #Dark fence
	p[192,0] = 398  #Acacia fence
	p[198,0] = 398  #End rod
	p[199,0] = 398  #Chorus flower
	p[200,0] = 398  #Purpur block
	p[201,0] = 398  #Purpur pillar
	p[202,0] = 398  #Purpur stairs
	p[203,0] = 398  #purpur slab
	p[204,0] = 398  #End stone
	p[208,0] = 398  #Grass path
	p[213,0] = 398  #Magma block
	p[214,0] = 398  #Nether wart block
	p[215,0] = 398  #Red nether brick
	p[216,0] = 398  #Bone block
	p[218,0] = 398  #Observer
	if options["Game version"] == "1.12+":
		p[251,0] = 398   #concrete
		p[251,1] = 398   #concrete
		p[251,2] = 398   #concrete
		p[251,3] = 398   #concrete
		p[251,4] = 398   #concrete
		p[251,5] = 398   #concrete
		p[251,6] = 398   #concrete
		p[251,7] = 398   #concrete
		p[251,8] = 398   #concrete
		p[251,9] = 398   #concrete
		p[251,10] = 398  #concrete
		p[251,11] = 398  #concrete
		p[251,12] = 398  #concrete
		p[251,13] = 398  #concrete
		p[251,14] = 398  #concrete
		p[251,15] = 398  #concrete
		p[252,0] = 398   #concrete powder
		p[252,1] = 398   #concrete powder
		p[252,2] = 398   #concrete powder
		p[252,3] = 398   #concrete powder
		p[252,4] = 398   #concrete powder
		p[252,5] = 398   #concrete powder
		p[252,6] = 398   #concrete powder
		p[252,7] = 398   #concrete powder
		p[252,8] = 398   #concrete powder
		p[252,9] = 398   #concrete powder
		p[252,10] = 398  #concrete powder
		p[252,11] = 398  #concrete powder
		p[252,12] = 398  #concrete powder
		p[252,13] = 398  #concrete powder
		p[252,14] = 398  #concrete powder
		p[252,15] = 398  #concrete powder
		p[235,1] = 398   #glazed terracotta
		p[236,1] = 398   #glazed terracotta
		p[237,1] = 398   #glazed terracotta
		p[238,1] = 398   #glazed terracotta
		p[239,1] = 398   #glazed terracotta
		p[240,1] = 398   #glazed terracotta
		p[241,1] = 398   #glazed terracotta
		p[242,1] = 398   #glazed terracotta
		p[243,1] = 398   #glazed terracotta
		p[244,1] = 398   #glazed terracotta
		p[245,1] = 398   #glazed terracotta
		p[246,1] = 398   #glazed terracotta
		p[247,1] = 398   #glazed terracotta
		p[248,1] = 398   #glazed terracotta
		p[249,1] = 398   #glazed terracotta
		p[250,1] = 398   #glazed terracotta	
	
	if chests:
		p[54,3] = spawnchanceChest #Chest
	if spawners:
		p[52,0] = spawnchanceSpawner #spawner
	return p
