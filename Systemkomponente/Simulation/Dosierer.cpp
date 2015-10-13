/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Dosierer
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Dosierer.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX

#define _OMSTATECHART_ANIMATED
//#]

//## auto_generated
#include "Dosierer.h"
//## link itsStation
#include "Station.h"
//## link itsVorrat
#include "Vorrat.h"
//#[ ignore
#define System_Dosierer_Dosierer_SERIALIZE OM_NO_OP

#define System_Dosierer_dosiere_SERIALIZE OM_NO_OP
//#]

//## package System

//## class Dosierer
Dosierer::Dosierer(IOxfActive* theActiveContext) : DosierMenge(1) {
    NOTIFY_REACTIVE_CONSTRUCTOR(Dosierer, Dosierer(), 0, System_Dosierer_Dosierer_SERIALIZE);
    setActiveContext(theActiveContext, false);
    itsStation = NULL;
    itsVorrat = NULL;
    initStatechart();
}

Dosierer::~Dosierer() {
    NOTIFY_DESTRUCTOR(~Dosierer, true);
    cleanUpRelations();
    cancelTimeouts();
}

void Dosierer::dosiere() {
    NOTIFY_OPERATION(dosiere, dosiere(), 0, System_Dosierer_dosiere_SERIALIZE);
    //#[ operation dosiere()
    int aMenge = DosierMenge;
    
    aMenge = itsVorrat->entnehme(aMenge);
    itsStation->dosiere(aMenge);
    //#]
}

int Dosierer::getDosierMenge() const {
    return DosierMenge;
}

void Dosierer::setDosierMenge(int p_DosierMenge) {
    DosierMenge = p_DosierMenge;
}

int Dosierer::getRunde() const {
    return runde;
}

void Dosierer::setRunde(int p_runde) {
    runde = p_runde;
}

Station* Dosierer::getItsStation() const {
    return itsStation;
}

void Dosierer::setItsStation(Station* p_Station) {
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

Vorrat* Dosierer::getItsVorrat() const {
    return itsVorrat;
}

void Dosierer::setItsVorrat(Vorrat* p_Vorrat) {
    itsVorrat = p_Vorrat;
    if(p_Vorrat != NULL)
        {
            NOTIFY_RELATION_ITEM_ADDED("itsVorrat", p_Vorrat, false, true);
        }
    else
        {
            NOTIFY_RELATION_CLEARED("itsVorrat");
        }
}

bool Dosierer::startBehavior() {
    bool done = false;
    done = OMReactive::startBehavior();
    return done;
}

void Dosierer::initStatechart() {
    rootState_subState = OMNonState;
    rootState_active = OMNonState;
    rootState_timeout = NULL;
}

void Dosierer::cleanUpRelations() {
    if(itsStation != NULL)
        {
            NOTIFY_RELATION_CLEARED("itsStation");
            itsStation = NULL;
        }
    if(itsVorrat != NULL)
        {
            NOTIFY_RELATION_CLEARED("itsVorrat");
            itsVorrat = NULL;
        }
}

void Dosierer::cancelTimeouts() {
    cancel(rootState_timeout);
}

bool Dosierer::cancelTimeout(const IOxfTimeout* arg) {
    bool res = false;
    if(rootState_timeout == arg)
        {
            rootState_timeout = NULL;
            res = true;
        }
    return res;
}

void Dosierer::rootState_entDef() {
    {
        NOTIFY_STATE_ENTERED("ROOT");
        NOTIFY_TRANSITION_STARTED("0");
        NOTIFY_STATE_ENTERED("ROOT.Idle");
        rootState_subState = Idle;
        rootState_active = Idle;
        NOTIFY_TRANSITION_TERMINATED("0");
    }
}

IOxfReactive::TakeEventStatus Dosierer::rootState_processEvent() {
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
                    dosiere();
                    //#]
                    rootState_timeout = scheduleTimeout(100, "ROOT.Running");
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
                            //#[ transition 3 
                            runde++;
                            //#]
                            NOTIFY_STATE_ENTERED("ROOT.Running");
                            rootState_subState = Running;
                            rootState_active = Running;
                            //#[ state Running.(Entry) 
                            dosiere();
                            //#]
                            rootState_timeout = scheduleTimeout(100, "ROOT.Running");
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
void OMAnimatedDosierer::serializeAttributes(AOMSAttributes* aomsAttributes) const {
    aomsAttributes->addAttribute("DosierMenge", x2String(myReal->DosierMenge));
    aomsAttributes->addAttribute("runde", x2String(myReal->runde));
}

void OMAnimatedDosierer::serializeRelations(AOMSRelations* aomsRelations) const {
    aomsRelations->addRelation("itsVorrat", false, true);
    if(myReal->itsVorrat)
        {
            aomsRelations->ADD_ITEM(myReal->itsVorrat);
        }
    aomsRelations->addRelation("itsStation", false, true);
    if(myReal->itsStation)
        {
            aomsRelations->ADD_ITEM(myReal->itsStation);
        }
}

void OMAnimatedDosierer::rootState_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT");
    switch (myReal->rootState_subState) {
        case Dosierer::Idle:
        {
            Idle_serializeStates(aomsState);
        }
        break;
        case Dosierer::Running:
        {
            Running_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedDosierer::Running_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Running");
}

void OMAnimatedDosierer::Idle_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Idle");
}
//#]

IMPLEMENT_REACTIVE_META_P(Dosierer, System, System, false, OMAnimatedDosierer)
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: Systemkomponente/Simulation/Dosierer.cpp
*********************************************************************/
