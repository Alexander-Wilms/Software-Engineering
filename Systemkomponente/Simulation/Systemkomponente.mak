
############# Target type (Debug/Release) ##################
############################################################
CPPCompileDebug=-g
CPPCompileRelease=-O
LinkDebug=-g
LinkRelease=-O

ConfigurationCPPCompileSwitches=   $(INCLUDE_QUALIFIER). $(INCLUDE_QUALIFIER)$(OMROOT) $(INCLUDE_QUALIFIER)$(OMROOT)/LangCpp $(INCLUDE_QUALIFIER)$(OMROOT)/LangCpp/oxf $(DEFINE_QUALIFIER)CYGWIN $(INST_FLAGS) $(INCLUDE_PATH) $(INST_INCLUDES) -Wno-write-strings $(CPPCompileDebug) -c 
ConfigurationCCCompileSwitches=$(INCLUDE_PATH) -c 

#########################################
###### Predefined macros ################
RM=/bin/rm -rf
INCLUDE_QUALIFIER=-I
DEFINE_QUALIFIER=-D
CC=g++
LIB_CMD=ar
LINK_CMD=g++
LIB_FLAGS=rvu
LINK_FLAGS= $(LinkDebug)   

#########################################
####### Context macros ##################

FLAGSFILE=
RULESFILE=
OMROOT="C:/Users/Alexander Wilms/IBM/Rational/Rhapsody/8.1.3/Share"
RHPROOT="C:/Program Files (x86)/IBM/Rational/Rhapsody/8.1.3"

CPP_EXT=.cpp
H_EXT=.h
OBJ_EXT=.o
EXE_EXT=.exe
LIB_EXT=.a

INSTRUMENTATION=Animation

TIME_MODEL=RealTime

TARGET_TYPE=Executable

TARGET_NAME=Systemkomponente

all : $(TARGET_NAME)$(EXE_EXT) Systemkomponente.mak

TARGET_MAIN=MainSystemkomponente

LIBS=

INCLUDE_PATH= \
  $(INCLUDE_QUALIFIER)$(OMROOT)/LangCpp/osconfig/Cygwin

ADDITIONAL_OBJS=

OBJS= \
  Caipisystem.o \
  Karussell.o \
  EinAusgabe.o \
  Abfuellstation.o \
  Stampfer.o \
  Station.o \
  Waage.o \
  Led.o \
  Tuer.o \
  Vorrat.o \
  Dosierer.o \
  Zucker.o \
  Cachacca.o \
  Limetten.o \
  Eis.o \
  Lichtschranke.o \
  Kolben.o \
  Limettenschneider.o \
  System.o




#########################################
####### Predefined macros ###############
$(OBJS) : $(INST_LIBS) $(OXF_LIBS)

ifeq ($(INSTRUMENTATION),Animation)

INST_FLAGS=$(DEFINE_QUALIFIER)OMANIMATOR $(DEFINE_QUALIFIER)__USE_W32_SOCKETS 
INST_INCLUDES=$(INCLUDE_QUALIFIER)$(OMROOT)/LangCpp/aom $(INCLUDE_QUALIFIER)$(OMROOT)/LangCpp/tom
INST_LIBS=$(OMROOT)/LangCpp/lib/cygwinaomanim$(LIB_EXT) $(OMROOT)/LangCpp/lib/cygwinoxsiminst$(LIB_EXT)
OXF_LIBS=$(OMROOT)/LangCpp/lib/cygwinoxfinst$(LIB_EXT) $(OMROOT)/LangCpp/lib/cygwinomcomappl$(LIB_EXT)
SOCK_LIB=-lws2_32

else
ifeq ($(INSTRUMENTATION),Tracing)

INST_FLAGS=$(DEFINE_QUALIFIER)OMTRACER 
INST_INCLUDES=$(INCLUDE_QUALIFIER)$(OMROOT)/LangCpp/aom $(INCLUDE_QUALIFIER)$(OMROOT)/LangCpp/tom
INST_LIBS=$(OMROOT)/LangCpp/lib/cygwintomtrace$(LIB_EXT) $(OMROOT)/LangCpp/lib/cygwinaomtrace$(LIB_EXT) $(OMROOT)/LangCpp/lib/cygwinoxsiminst$(LIB_EXT)
OXF_LIBS=$(OMROOT)/LangCpp/lib/cygwinoxfinst$(LIB_EXT) $(OMROOT)/LangCpp/lib/cygwinomcomappl$(LIB_EXT)
SOCK_LIB=-lws2_32

else
ifeq ($(INSTRUMENTATION),None)

INST_FLAGS= 
INST_INCLUDES=
INST_LIBS=$(OMROOT)/LangCpp/lib/cygwinoxsim$(LIB_EXT)
OXF_LIBS=$(OMROOT)/LangCpp/lib/cygwinoxf$(LIB_EXT)
SOCK_LIB=-lws2_32

else
	@echo An invalid Instrumentation $(INSTRUMENTATION) is specified.
	exit
endif
endif
endif

.SUFFIXES: $(CPP_EXT)

#####################################################################
##################### Context dependencies and commands #############






Caipisystem.o : Caipisystem.cpp Caipisystem.h    System.h Karussell.h Waage.h Led.h EinAusgabe.h Limetten.h Zucker.h Cachacca.h Eis.h Lichtschranke.h Stampfer.h Station.h Tuer.h Kolben.h Abfuellstation.h Dosierer.h Vorrat.h 
	@echo Compiling Caipisystem.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o Caipisystem.o Caipisystem.cpp




Karussell.o : Karussell.cpp Karussell.h    System.h Station.h Waage.h Led.h 
	@echo Compiling Karussell.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o Karussell.o Karussell.cpp




EinAusgabe.o : EinAusgabe.cpp EinAusgabe.h    System.h Station.h Tuer.h Karussell.h Waage.h Kolben.h 
	@echo Compiling EinAusgabe.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o EinAusgabe.o EinAusgabe.cpp




Abfuellstation.o : Abfuellstation.cpp Abfuellstation.h    System.h Dosierer.h Vorrat.h Station.h Tuer.h Karussell.h Waage.h Kolben.h 
	@echo Compiling Abfuellstation.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o Abfuellstation.o Abfuellstation.cpp




Stampfer.o : Stampfer.cpp Stampfer.h    System.h Kolben.h Station.h Tuer.h Karussell.h Waage.h 
	@echo Compiling Stampfer.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o Stampfer.o Stampfer.cpp




Station.o : Station.cpp Station.h    System.h Tuer.h Karussell.h Waage.h Kolben.h 
	@echo Compiling Station.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o Station.o Station.cpp




Waage.o : Waage.cpp Waage.h    System.h 
	@echo Compiling Waage.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o Waage.o Waage.cpp




Led.o : Led.cpp Led.h    System.h 
	@echo Compiling Led.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o Led.o Led.cpp




Tuer.o : Tuer.cpp Tuer.h    System.h 
	@echo Compiling Tuer.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o Tuer.o Tuer.cpp




Vorrat.o : Vorrat.cpp Vorrat.h    System.h 
	@echo Compiling Vorrat.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o Vorrat.o Vorrat.cpp




Dosierer.o : Dosierer.cpp Dosierer.h    System.h Vorrat.h Station.h 
	@echo Compiling Dosierer.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o Dosierer.o Dosierer.cpp




Zucker.o : Zucker.cpp Zucker.h    System.h Abfuellstation.h Dosierer.h Vorrat.h Station.h Tuer.h Karussell.h Waage.h Kolben.h 
	@echo Compiling Zucker.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o Zucker.o Zucker.cpp




Cachacca.o : Cachacca.cpp Cachacca.h    System.h Abfuellstation.h Dosierer.h Vorrat.h Station.h Tuer.h Karussell.h Waage.h Kolben.h 
	@echo Compiling Cachacca.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o Cachacca.o Cachacca.cpp




Limetten.o : Limetten.cpp Limetten.h    System.h Limettenschneider.h Kolben.h Lichtschranke.h Abfuellstation.h Dosierer.h Vorrat.h Station.h Tuer.h Karussell.h Waage.h 
	@echo Compiling Limetten.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o Limetten.o Limetten.cpp




Eis.o : Eis.cpp Eis.h    System.h Abfuellstation.h Dosierer.h Vorrat.h Station.h Tuer.h Karussell.h Waage.h Kolben.h 
	@echo Compiling Eis.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o Eis.o Eis.cpp




Lichtschranke.o : Lichtschranke.cpp Lichtschranke.h    System.h Limetten.h Station.h 
	@echo Compiling Lichtschranke.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o Lichtschranke.o Lichtschranke.cpp




Kolben.o : Kolben.cpp Kolben.h    System.h Station.h 
	@echo Compiling Kolben.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o Kolben.o Kolben.cpp




Limettenschneider.o : Limettenschneider.cpp Limettenschneider.h    System.h Kolben.h Station.h 
	@echo Compiling Limettenschneider.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o Limettenschneider.o Limettenschneider.cpp




System.o : System.cpp System.h    Caipisystem.h Karussell.h EinAusgabe.h Abfuellstation.h Stampfer.h Station.h Waage.h Led.h Tuer.h Vorrat.h Dosierer.h Zucker.h Cachacca.h Limetten.h Eis.h Lichtschranke.h Kolben.h Limettenschneider.h 
	@echo Compiling System.cpp
	@$(CC) $(ConfigurationCPPCompileSwitches)  -o System.o System.cpp







$(TARGET_MAIN)$(OBJ_EXT) : $(TARGET_MAIN)$(CPP_EXT) $(OBJS)
	@echo Compiling $(TARGET_MAIN)$(CPP_EXT)
	@$(CC) $(ConfigurationCPPCompileSwitches) -o  $(TARGET_MAIN)$(OBJ_EXT) $(TARGET_MAIN)$(CPP_EXT)

####################################################################
############## Predefined Instructions #############################
$(TARGET_NAME)$(EXE_EXT): $(OBJS) $(ADDITIONAL_OBJS) $(TARGET_MAIN)$(OBJ_EXT) Systemkomponente.mak
	@echo Linking $(TARGET_NAME)$(EXE_EXT)
	@$(LINK_CMD)  $(TARGET_MAIN)$(OBJ_EXT) $(OBJS) $(ADDITIONAL_OBJS) \
	$(LIBS) \
	$(OXF_LIBS) \
	$(INST_LIBS) \
	$(OXF_LIBS) \
	$(INST_LIBS) \
	$(SOCK_LIB) \
	$(LINK_FLAGS) -o $(TARGET_NAME)$(EXE_EXT)

$(TARGET_NAME)$(LIB_EXT) : $(OBJS) $(ADDITIONAL_OBJS) Systemkomponente.mak
	@echo Building library $@
	@$(LIB_CMD) $(LIB_FLAGS) $(TARGET_NAME)$(LIB_EXT) $(OBJS) $(ADDITIONAL_OBJS)



clean:
	@echo Cleanup
	$(RM) Caipisystem.o
	$(RM) Karussell.o
	$(RM) EinAusgabe.o
	$(RM) Abfuellstation.o
	$(RM) Stampfer.o
	$(RM) Station.o
	$(RM) Waage.o
	$(RM) Led.o
	$(RM) Tuer.o
	$(RM) Vorrat.o
	$(RM) Dosierer.o
	$(RM) Zucker.o
	$(RM) Cachacca.o
	$(RM) Limetten.o
	$(RM) Eis.o
	$(RM) Lichtschranke.o
	$(RM) Kolben.o
	$(RM) Limettenschneider.o
	$(RM) System.o
	$(RM) $(TARGET_MAIN)$(OBJ_EXT) $(ADDITIONAL_OBJS)
	$(RM) $(TARGET_NAME)$(LIB_EXT)
	$(RM) $(TARGET_NAME)$(EXE_EXT)

