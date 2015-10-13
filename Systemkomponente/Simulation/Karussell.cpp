/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Karussell
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Karussell.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX

#define _OMSTATECHART_ANIMATED
//#]

//## auto_generated
#include "Karussell.h"
//## link itsLed
#include "Led.h"
//## link itsStation
#include "Station.h"
//## link itsWaage
#include "Waage.h"
//#[ ignore
#define System_Karussell_addWaage_SERIALIZE \
    aomsmethod->addAttribute("aWaage", x2String(aWaage));\
    aomsmethod->addAttribute("aMenge", x2String(aMenge));
#define System_Karussell_Karussell_SERIALIZE OM_NO_OP

#define System_Karussell_GlaeserDrauf_SERIALIZE OM_NO_OP

#define System_Karussell_clearBrutto_SERIALIZE aomsmethod->addAttribute("aWaage", x2String(aWaage));

#define System_Karussell_drehen_SERIALIZE OM_NO_OP

#define System_Karussell_getBrutto_SERIALIZE aomsmethod->addAttribute("aWaage", x2String(aWaage));

#define System_Karussell_getNetto_SERIALIZE aomsmethod->addAttribute("aWaage", x2String(aWaage));

#define System_Karussell_setTara_SERIALIZE aomsmethod->addAttribute("aWaage", x2String(aWaage));

#define System_Karussell_updateLED_SERIALIZE OM_NO_OP
//#]

//## package System

//## class Karussell
Karussell::Karussell(IOxfActive* theActiveContext) : jemalsgedreht(false) {
    NOTIFY_REACTIVE_CONSTRUCTOR(Karussell, Karussell(), 0, System_Karussell_Karussell_SERIALIZE);
    setActiveContext(theActiveContext, false);
    {
        for (int pos = 0; pos < 6; ++pos) {
        	itsLed[pos] = NULL;
        }
    }
    {
        for (int pos = 0; pos < 6; ++pos) {
        	itsStation[pos] = NULL;
        }
    }
    {
        for (int pos = 0; pos < 6; ++pos) {
        	itsWaage[pos] = NULL;
        }
    }
    initStatechart();
}

Karussell::~Karussell() {
    NOTIFY_DESTRUCTOR(~Karussell, true);
    cleanUpRelations();
    cancelTimeouts();
}

int Karussell::GlaeserDrauf() {
    NOTIFY_OPERATION(GlaeserDrauf, GlaeserDrauf(), 0, System_Karussell_GlaeserDrauf_SERIALIZE);
    //#[ operation GlaeserDrauf()
    int anz = 0;
    for(int i = 0; i < MaxStation; i++) {
    	anz += itsWaage[i]->getBrutto() >= GlasGewicht; 
    } 
    // std::cout << "Anzahl Glaeser: " << anz << std::endl;      
    return anz;
    //#]
}

void Karussell::addWaage(int aWaage, int aMenge) {
    NOTIFY_OPERATION(addWaage, addWaage(int,int), 2, System_Karussell_addWaage_SERIALIZE);
    //#[ operation addWaage(int,int)
    itsWaage[aWaage]->addBrutto(aMenge);
    //#]
}

void Karussell::clearBrutto(int aWaage) {
    NOTIFY_OPERATION(clearBrutto, clearBrutto(int), 1, System_Karussell_clearBrutto_SERIALIZE);
    //#[ operation clearBrutto(int)
    return itsWaage[aWaage]->clearBrutto();
    //#]
}

void Karussell::drehen() {
    NOTIFY_OPERATION(drehen, drehen(), 0, System_Karussell_drehen_SERIALIZE);
    //#[ operation drehen()
    Waage* myWaage = itsWaage[MaxStation-1]; 
    
    if( !GlaeserDrauf() ) return;
    
    for(int i=0; i < MaxStation; i++) 
    {
    	if( !itsStation[i]->isOk() ) return; 
    }
    
    for( int i = MaxStation-1; i > 0; i-- )
    {
    	itsWaage[i] = itsWaage[i-1];
    	
    }
    itsWaage[0] = myWaage;  
     
    updateLED();
     
    for(int i=0; i < MaxStation; i++) 
    {
    	itsStation[i]->GEN(evRun); 
    }
    
    jemalsgedreht = true;         
    //#]
}

int Karussell::getBrutto(int aWaage) {
    NOTIFY_OPERATION(getBrutto, getBrutto(int), 1, System_Karussell_getBrutto_SERIALIZE);
    //#[ operation getBrutto(int)
    return itsWaage[aWaage]->getBrutto();
    //#]
}

int Karussell::getNetto(int aWaage) {
    NOTIFY_OPERATION(getNetto, getNetto(int), 1, System_Karussell_getNetto_SERIALIZE);
    //#[ operation getNetto(int)
    return itsWaage[aWaage]->getNetto();
    //#]
}

void Karussell::setTara(int aWaage) {
    NOTIFY_OPERATION(setTara, setTara(int), 1, System_Karussell_setTara_SERIALIZE);
    //#[ operation setTara(int)
    return itsWaage[aWaage]->setTara();
    //#]
}

void Karussell::updateLED() {
    NOTIFY_OPERATION(updateLED, updateLED(), 0, System_Karussell_updateLED_SERIALIZE);
    //#[ operation updateLED()
    for(int i=0; i < MaxStation; i++) 
    {
    	itsLed[i]->setOn(itsWaage[i]->getBrutto() >= GlasGewicht); 
    }
    //#]
}

bool Karussell::getDreht() const {
    return dreht;
}

void Karussell::setDreht(bool p_dreht) {
    dreht = p_dreht;
    NOTIFY_SET_OPERATION;
}

bool Karussell::getJemalsgedreht() const {
    return jemalsgedreht;
}

void Karussell::setJemalsgedreht(bool p_jemalsgedreht) {
    jemalsgedreht = p_jemalsgedreht;
}

int Karussell::getItsLed() const {
    int iter = 0;
    return iter;
}

void Karussell::addItsLed(Led* p_Led) {
    if(p_Led != NULL)
        {
            NOTIFY_RELATION_ITEM_ADDED("itsLed", p_Led, false, false);
        }
    else
        {
            NOTIFY_RELATION_CLEARED("itsLed");
        }
    for (int pos = 0; pos < 6; ++pos) {
    	if (!itsLed[pos]) {
    		itsLed[pos] = p_Led;
    		break;
    	}
    }
}

void Karussell::removeItsLed(Led* p_Led) {
    NOTIFY_RELATION_ITEM_REMOVED("itsLed", p_Led);
    for (int pos = 0; pos < 6; ++pos) {
    	if (itsLed[pos] == p_Led) {
    		itsLed[pos] = NULL;
    	}
    }
}

void Karussell::clearItsLed() {
    NOTIFY_RELATION_CLEARED("itsLed");
    
}

int Karussell::getItsStation() const {
    int iter = 0;
    return iter;
}

void Karussell::addItsStation(Station* p_Station) {
    if(p_Station != NULL)
        {
            p_Station->_setItsKarussell(this);
        }
    _addItsStation(p_Station);
}

void Karussell::removeItsStation(Station* p_Station) {
    if(p_Station != NULL)
        {
            p_Station->__setItsKarussell(NULL);
        }
    _removeItsStation(p_Station);
}

void Karussell::clearItsStation() {
    int iter = 0;
    while ((iter < 6) && itsStation[iter]){
        (itsStation[iter])->_clearItsKarussell();
        iter++;
    }
    _clearItsStation();
}

int Karussell::getItsWaage() const {
    int iter = 0;
    return iter;
}

void Karussell::addItsWaage(Waage* p_Waage) {
    if(p_Waage != NULL)
        {
            NOTIFY_RELATION_ITEM_ADDED("itsWaage", p_Waage, false, false);
        }
    else
        {
            NOTIFY_RELATION_CLEARED("itsWaage");
        }
    for (int pos = 0; pos < 6; ++pos) {
    	if (!itsWaage[pos]) {
    		itsWaage[pos] = p_Waage;
    		break;
    	}
    }
}

void Karussell::removeItsWaage(Waage* p_Waage) {
    NOTIFY_RELATION_ITEM_REMOVED("itsWaage", p_Waage);
    for (int pos = 0; pos < 6; ++pos) {
    	if (itsWaage[pos] == p_Waage) {
    		itsWaage[pos] = NULL;
    	}
    }
}

void Karussell::clearItsWaage() {
    NOTIFY_RELATION_CLEARED("itsWaage");
    
}

bool Karussell::startBehavior() {
    bool done = false;
    done = OMReactive::startBehavior();
    return done;
}

void Karussell::initStatechart() {
    rootState_subState = OMNonState;
    rootState_active = OMNonState;
    rootState_timeout = NULL;
}

void Karussell::cleanUpRelations() {
    
    {
        int iter = 0;
        while ((iter < 6) && itsStation[iter]){
            Karussell* p_Karussell = (itsStation[iter])->getItsKarussell();
            if(p_Karussell != NULL)
                {
                    (itsStation[iter])->__setItsKarussell(NULL);
                }
            iter++;
        }
    }
    
}

void Karussell::cancelTimeouts() {
    cancel(rootState_timeout);
}

bool Karussell::cancelTimeout(const IOxfTimeout* arg) {
    bool res = false;
    if(rootState_timeout == arg)
        {
            rootState_timeout = NULL;
            res = true;
        }
    return res;
}

void Karussell::_addItsStation(Station* p_Station) {
    if(p_Station != NULL)
        {
            NOTIFY_RELATION_ITEM_ADDED("itsStation", p_Station, false, false);
        }
    else
        {
            NOTIFY_RELATION_CLEARED("itsStation");
        }
    for (int pos = 0; pos < 6; ++pos) {
    	if (!itsStation[pos]) {
    		itsStation[pos] = p_Station;
    		break;
    	}
    }
}

void Karussell::_removeItsStation(Station* p_Station) {
    NOTIFY_RELATION_ITEM_REMOVED("itsStation", p_Station);
    for (int pos = 0; pos < 6; ++pos) {
    	if (itsStation[pos] == p_Station) {
    		itsStation[pos] = NULL;
    	}
    }
}

void Karussell::_clearItsStation() {
    NOTIFY_RELATION_CLEARED("itsStation");
    
}

void Karussell::rootState_entDef() {
    {
        NOTIFY_STATE_ENTERED("ROOT");
        NOTIFY_TRANSITION_STARTED("0");
        NOTIFY_STATE_ENTERED("ROOT.idle");
        rootState_subState = idle;
        rootState_active = idle;
        //#[ state idle.(Entry) 
           dreht = false;
        //#]
        rootState_timeout = scheduleTimeout(1000, "ROOT.idle");
        NOTIFY_TRANSITION_TERMINATED("0");
    }
}

IOxfReactive::TakeEventStatus Karussell::rootState_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    // State idle
    if(rootState_active == idle)
        {
            if(IS_EVENT_TYPE_OF(OMTimeoutEventId))
                {
                    if(getCurrentEvent() == rootState_timeout)
                        {
                            NOTIFY_TRANSITION_STARTED("1");
                            cancel(rootState_timeout);
                            //#[ state idle.(Exit) 
                            dreht = true;  
                            //#]
                            NOTIFY_STATE_EXITED("ROOT.idle");
                            //#[ transition 1 
                            drehen();
                            //#]
                            NOTIFY_STATE_ENTERED("ROOT.idle");
                            rootState_subState = idle;
                            rootState_active = idle;
                            //#[ state idle.(Entry) 
                               dreht = false;
                            //#]
                            rootState_timeout = scheduleTimeout(1000, "ROOT.idle");
                            NOTIFY_TRANSITION_TERMINATED("1");
                            res = eventConsumed;
                        }
                }
            
        }
    return res;
}

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedKarussell::serializeAttributes(AOMSAttributes* aomsAttributes) const {
    aomsAttributes->addAttribute("dreht", x2String(myReal->dreht));
    aomsAttributes->addAttribute("jemalsgedreht", x2String(myReal->jemalsgedreht));
}

void OMAnimatedKarussell::serializeRelations(AOMSRelations* aomsRelations) const {
    aomsRelations->addRelation("itsStation", false, false);
    {
        int iter = 0;
        while ((iter < 6) && myReal->itsStation[iter]){
            aomsRelations->ADD_ITEM(myReal->itsStation[iter]);
            iter++;
        }
    }
    aomsRelations->addRelation("itsWaage", false, false);
    {
        int iter = 0;
        while ((iter < 6) && myReal->itsWaage[iter]){
            aomsRelations->ADD_ITEM(myReal->itsWaage[iter]);
            iter++;
        }
    }
    aomsRelations->addRelation("itsLed", false, false);
    {
        int iter = 0;
        while ((iter < 6) && myReal->itsLed[iter]){
            aomsRelations->ADD_ITEM(myReal->itsLed[iter]);
            iter++;
        }
    }
}

void OMAnimatedKarussell::rootState_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT");
    if(myReal->rootState_subState == Karussell::idle)
        {
            idle_serializeStates(aomsState);
        }
}

void OMAnimatedKarussell::idle_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.idle");
}
//#]

IMPLEMENT_REACTIVE_META_P(Karussell, System, System, false, OMAnimatedKarussell)
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: Systemkomponente/Simulation/Karussell.cpp
*********************************************************************/
