import os

i = 0

folder = "Box_L0040A_N0256_CPla"
path = "/home/kaurov/kaurov/LGadget/Bens/"

for i in range(101):
    stri = '%03i'%i
    print(stri)
    os.system('mkdir '+path+folder+'/'+stri)
    temp='''[ConvertSnapshot]
#######################
# Required Parameters #
#######################
Input = '''+path+folder+'''/snapdir_'''+stri+'''
Output = '''+path+folder+'''/'''+stri+'''
InputFormat = LGadget-2
Cells = 8 # It's unlikely that you will want to change this.
#######################
# Optional Parameters #
#######################
# ProfileFile = pprof.out
LogFile = log.out
# IteratedInput = path/to/iterated/input_with_single_%d_format
# IteratedOutput = path/to/iterated/input_with_single_%d_format
# IterationStart = 0
# IterationEnd = 100
# Inclusive. If IterationEnd isn't set, folders will be iterated through until
# an invalid one is found.'''
    f = open('convert_config.txt','w')
    f.write(temp)
    f.close()
    os.system('./main -ConvertSnapshot convert_config.txt')
    os.system('mkdir '+path+folder+'/'+stri+'r')
    temp='''[Render]

######################
# RequiredParameters #
######################

# Quantity can be set to one of:
# [ Density | Velocity | DensityGradient | VelocityCurl | VelocityDivergence ].
Quantity = Density

Input  = '''+path+folder+'''/'''+stri+'''
Output = '''+path+folder+'''/'''+stri+'''r

# Default way of specifying pixel size: the number of pixels which would
# be required to render the entire box. All rendered boxes will have the same
# pixel size.
TotalPixels = 256

# Default way of specifying particle count: the number of particles per
# tetrahedron.
Particles = 25

#####################
# OptionalParamters #
#####################

# Alternative way of specifying pixel size: the number of pixels required to
# render the longest axis of each box. All rendered boxes will, in general,
# not have the same number of pixels.
# ImagePixels = 100

# Alternative way of specifying the particle count. gotetra will (attempt to)
# automatically calculate how many particles are needed so that all projections
# rendered from the resulting grid will have enough particles-per-tetrahedron
# to avoid artifacts.
# AutoParticles = true

# Alternative way of specifying the particle count. Identical to specifying
# AutoParticles, except that projections with a depth below ProjectionDepth
# may contain artifacts.
# ProjectionDepth = 3

# ProfileFile = prof.out
# LogFile = log.out

# SubsampleLength = 2

# Will result in files named pre_*foo*_app.gtet:
# PrependName = pre_
# AppendName  = _app'''
    f = open('render_config.txt','w')
    f.write(temp)
    f.close()
    temp='''[Box "my_z_slice"]
# A thin slice containing a big halo for the L0125 box.

#######################
# Required Parameters #
#######################

# Location of lowermost corner:
X = 0.
Y = 0.
Z = 0.

XWidth = 39.9999999999999
YWidth = 39.9999999999999
ZWidth = 39.9999999999999'''
    f = open('bounds.txt','w')
    f.write(temp)
    f.close()
    os.system('./main -Render render_config.txt bounds.txt')
