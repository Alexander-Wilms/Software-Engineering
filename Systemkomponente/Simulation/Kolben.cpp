/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Kolben
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Kolben.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX

#define _OMSTATECHART_ANIMATED
//#]

//## auto_generated
#include "Kolben.h"
//## link itsStation
#include "Station.h"
//#[ ignore
#define System_Kolben_Kolben_SERIALIZE OM_NO_OP

#define System_Kolben_getPosition_SERIALIZE OM_NO_OP

#define System_Kolben_run_SERIALIZE OM_NO_OP

#define System_Kolben_setDown_SERIALIZE aomsmethod->addAttribute("direction", x2String(direction));
//#]

//## package System

//## class Kolben
Kolben::Kolben(IOxfActive* theActiveContext) : Down(false), MaxPos(100), Pos(100) {
    NOTIFY_REACTIVE_CONSTRUCTOR(Kolben, Kolben(), 0, System_Kolben_Kolben_SERIALIZE);
    setActiveContext(theActiveContext, false);
    itsStation = NULL;
    initStatechart();
}

Kolben::~Kolben() {
    NOTIFY_DESTRUCTOR(~Kolben, true);
    cleanUpRelations();
    cancelTimeouts();
}

int Kolben::getPosition() {
    NOTIFY_OPERATION(getPosition, getPosition(), 0, System_Kolben_getPosition_SERIALIZE);
    //#[ operation getPosition()
    return Pos;
    //#]
}

void Kolben::run() {
    NOTIFY_OPERATION(run, run(), 0, System_Kolben_run_SERIALIZE);
    //#[ operation run()
    if(!Down && Pos < MaxPos)	Pos +=10;
    else if(Down && Pos > 0)	Pos -= 10;
    else if(!Down && Pos >= MaxPos) {   
    	itsStation->GEN(evReady);    
    }            
    else if(Down && Pos <= 0) {    
    
    	itsStation->GEN(evReady);
    } 
           
    
    //#]
}

void Kolben::setDown(bool direction) {
    NOTIFY_OPERATION(setDown, setDown(bool), 1, System_Kolben_setDown_SERIALIZE);
    //#[ operation setDown(bool)
    Down = direction;
    //#]
}

bool Kolben::getDown() const {
    return Down;
}

int Kolben::getMaxPos() const {
    return MaxPos;
}

void Kolben::setMaxPos(int p_MaxPos) {
    MaxPos = p_MaxPos;
}

int Kolben::getPos() const {
    return Pos;
}

void Kolben::setPos(int p_Pos) {
    Pos = p_Pos;
    NOTIFY_SET_OPERATION;
}

Station* Kolben::getItsStation() const {
    return itsStation;
}

void Kolben::setItsStation(Station* p_Station) {
    if(p_Station != NULL)
        {
            p_Station->_addItsKolben(this);
        }
    _setItsStation(p_Station);
}

bool Kolben::startBehavior() {
    bool done = false;
    done = OMReactive::startBehavior();
    return done;
}

void Kolben::initStatechart() {
    rootState_subState = OMNonState;
    rootState_active = OMNonState;
    rootState_timeout = NULL;
}

void Kolben::cleanUpRelations() {
    if(itsStation != NULL)
        {
            NOTIFY_RELATION_CLEARED("itsStation");
            Station* current = itsStation;
            if(current != NULL)
                {
                    current->_removeItsKolben(this);
                }
            itsStation = NULL;
        }
}

void Kolben::cancelTimeouts() {
    cancel(rootState_timeout);
}

bool Kolben::cancelTimeout(const IOxfTimeout* arg) {
    bool res = false;
    if(rootState_timeout == arg)
        {
            rootState_timeout = NULL;
            res = true;
        }
    return res;
}

void Kolben::__setItsStation(Station* p_Station) {
    itsStation = p_Station;
    if(p_Station != NULL)
        {
            NOTIFY_RELATION_ITEM_ADDED("itsStation", p_Station, false, true);
        }
    else
        {
            NOTIFY_RELATION_CLEARED("itsStation");
        }
}

void Kolben::_setItsStation(Station* p_Station) {
    if(itsStation != NULL)
        {
            itsStation->_removeItsKolben(this);
        }
    __setItsStation(p_Station);
}

void Kolben::_clearItsStation() {
    NOTIFY_RELATION_CLEARED("itsStation");
    itsStation = NULL;
}

void Kolben::rootState_entDef() {
    {
        NOTIFY_STATE_ENTERED("ROOT");
        NOTIFY_TRANSITION_STARTED("0");
        NOTIFY_STATE_ENTERED("ROOT.Idle");
        rootState_subState = Idle;
        rootState_active = Idle;
        NOTIFY_TRANSITION_TERMINATED("0");
    }
}

IOxfReactive::TakeEventStatus Kolben::rootState_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (rootState_active) {
        // State Idle
        case Idle:
        {
            if(IS_EVENT_TYPE_OF(evRun_System_id))
                {
                    NOTIFY_TRANSITION_STARTED("1");
                    NOTIFY_STATE_EXITED("ROOT.Idle");
                    NOTIFY_STATE_ENTERED("ROOT.Running");
                    rootState_subState = Running;
                    rootState_active = Running;
                    //#[ state Running.(Entry) 
                    run();
                    
                    //#]
                    rootState_timeout = scheduleTimeout(1, "ROOT.Running");
                    NOTIFY_TRANSITION_TERMINATED("1");
                    res = eventConsumed;
                }
            
        }
        break;
        // State Running
        case Running:
        {
            if(IS_EVENT_TYPE_OF(evStop_System_id))
                {
                    NOTIFY_TRANSITION_STARTED("2");
                    cancel(rootState_timeout);
                    NOTIFY_STATE_EXITED("ROOT.Running");
                    NOTIFY_STATE_ENTERED("ROOT.Idle");
                    rootState_subState = Idle;
                    rootState_active = Idle;
                    NOTIFY_TRANSITION_TERMINATED("2");
                    res = eventConsumed;
                }
            else if(IS_EVENT_TYPE_OF(OMTimeoutEventId))
                {
                    if(getCurrentEvent() == rootState_timeout)
                        {
                            NOTIFY_TRANSITION_STARTED("3");
                            cancel(rootState_timeout);
                            NOTIFY_STATE_EXITED("ROOT.Running");
                            NOTIFY_STATE_ENTERED("ROOT.Running");
                            rootState_subState = Running;
                            rootState_active = Running;
                            //#[ state Running.(Entry) 
                            run();
                            
                            //#]
                            rootState_timeout = scheduleTimeout(1, "ROOT.Running");
                            NOTIFY_TRANSITION_TERMINATED("3");
                            res = eventConsumed;
                        }
                }
            
        }
        break;
        default:
            break;
    }
    return res;
}

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedKolben::serializeAttributes(AOMSAttributes* aomsAttributes) const {
    aomsAttributes->addAttribute("Down", x2String(myReal->Down));
    aomsAttributes->addAttribute("Pos", x2String(myReal->Pos));
    aomsAttributes->addAttribute("MaxPos", x2String(myReal->MaxPos));
}

void OMAnimatedKolben::serializeRelations(AOMSRelations* aomsRelations) const {
    aomsRelations->addRelation("itsStation", false, true);
    if(myReal->itsStation)
        {
            aomsRelations->ADD_ITEM(myReal->itsStation);
        }
}

void OMAnimatedKolben::rootState_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT");
    switch (myReal->rootState_subState) {
        case Kolben::Idle:
        {
            Idle_serializeStates(aomsState);
        }
        break;
        case Kolben::Running:
        {
            Running_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedKolben::Running_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Running");
}

void OMAnimatedKolben::Idle_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Idle");
}
//#]

IMPLEMENT_REACTIVE_META_P(Kolben, System, System, false, OMAnimatedKolben)
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: Systemkomponente/Simulation/Kolben.cpp
*********************************************************************/
