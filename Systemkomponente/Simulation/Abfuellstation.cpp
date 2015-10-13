/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Abfuellstation
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Abfuellstation.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX

#define _OMSTATECHART_ANIMATED
//#]

//## auto_generated
#include "Abfuellstation.h"
//## auto_generated
#include "Karussell.h"
//## auto_generated
#include "Kolben.h"
//## auto_generated
#include "Waage.h"
//#[ ignore
#define System_Abfuellstation_Abfuellstation_SERIALIZE OM_NO_OP

#define System_Abfuellstation_fuellen_SERIALIZE OM_NO_OP

#define System_Abfuellstation_getitsVorrat_SERIALIZE OM_NO_OP
//#]

//## package System

//## class Abfuellstation
Abfuellstation::Abfuellstation(IOxfActive* theActiveContext) {
    NOTIFY_REACTIVE_CONSTRUCTOR(Abfuellstation, Abfuellstation(), 0, System_Abfuellstation_Abfuellstation_SERIALIZE);
    setActiveContext(theActiveContext, false);
    {
        {
            itsDosierer.setShouldDelete(false);
        }
    }
    initRelations();
    initStatechart();
    //#[ operation Abfuellstation()
    setDosierMenge(20); // Soviel wird ungefähr eingefüllt
    itsDosierer.setItsStation(this);
    //#]
}

Abfuellstation::~Abfuellstation() {
    NOTIFY_DESTRUCTOR(~Abfuellstation, false);
}

void Abfuellstation::fuellen() {
    NOTIFY_OPERATION(fuellen, fuellen(), 0, System_Abfuellstation_fuellen_SERIALIZE);
    //#[ operation fuellen()
    itsVorrat.fuelle();
    //#]
}

Vorrat* Abfuellstation::getitsVorrat() {
    NOTIFY_OPERATION(getitsVorrat, getitsVorrat(), 0, System_Abfuellstation_getitsVorrat_SERIALIZE);
    //#[ operation getitsVorrat()
    return &itsVorrat;
    //#]
}

Dosierer* Abfuellstation::getItsDosierer() const {
    return (Dosierer*) &itsDosierer;
}

Vorrat* Abfuellstation::getItsVorrat() const {
    return (Vorrat*) &itsVorrat;
}

bool Abfuellstation::startBehavior() {
    bool done = true;
    done &= Station::startBehavior();
    done &= itsDosierer.startBehavior();
    return done;
}

void Abfuellstation::initRelations() {
    itsDosierer.setItsVorrat(&itsVorrat);
}

void Abfuellstation::initStatechart() {
    rootState_subState = OMNonState;
    rootState_active = OMNonState;
    state_5_subState = OMNonState;
    state_5_active = OMNonState;
    state_4_subState = OMNonState;
    state_4_active = OMNonState;
}

void Abfuellstation::setActiveContext(IOxfActive* theActiveContext, bool activeInstance) {
    OMReactive::setActiveContext(theActiveContext, activeInstance);
    {
        itsDosierer.setActiveContext(theActiveContext, false);
    }
}

void Abfuellstation::destroy() {
    itsDosierer.destroy();
    Station::destroy();
}

void Abfuellstation::rootState_entDef() {
    {
        NOTIFY_STATE_ENTERED("ROOT");
        NOTIFY_TRANSITION_STARTED("9");
        Betrieb_entDef();
        NOTIFY_TRANSITION_TERMINATED("9");
    }
}

IOxfReactive::TakeEventStatus Abfuellstation::rootState_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    // State Betrieb
    if(rootState_active == Betrieb)
        {
            res = Betrieb_processEvent();
        }
    return res;
}

void Abfuellstation::Betrieb_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb");
    rootState_subState = Betrieb;
    rootState_active = Betrieb;
    state_4_entDef();
    state_5_entDef();
}

void Abfuellstation::Betrieb_exit() {
    switch (state_4_subState) {
        // State Idle
        case Idle:
        {
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Idle");
        }
        break;
        // State Running
        case Running:
        {
            popNullTransition();
            cancel(state_4_timeout);
            //#[ state Betrieb.state_4.Running.(Exit) 
            itsDosierer.GEN(evStop);
            //#]
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running");
        }
        break;
        // State Stopped
        case Stopped:
        {
            //#[ state Betrieb.state_4.Stopped.(Exit) 
            Error = false;
            //#]
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Stopped");
        }
        break;
        default:
            break;
    }
    state_4_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4");
    switch (state_5_subState) {
        // State Offen
        case Offen:
        {
            popNullTransition();
            cancel(state_5_timeout);
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_5.Offen");
        }
        break;
        // State Zu
        case Zu:
        {
            popNullTransition();
            cancel(state_5_timeout);
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_5.Zu");
        }
        break;
        default:
            break;
    }
    state_5_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_5");
    
    NOTIFY_STATE_EXITED("ROOT.Betrieb");
}

IOxfReactive::TakeEventStatus Abfuellstation::Betrieb_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    // State state_4
    if(state_4_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(Betrieb))
                {
                    return res;
                }
        }
    // State state_5
    if(state_5_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(Betrieb))
                {
                    return res;
                }
        }
    
    return res;
}

void Abfuellstation::state_5_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5");
    NOTIFY_TRANSITION_STARTED("10");
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5.Offen");
    pushNullTransition();
    state_5_subState = Offen;
    state_5_active = Offen;
    state_5_timeout = scheduleTimeout(500, "ROOT.Betrieb.state_5.Offen");
    NOTIFY_TRANSITION_TERMINATED("10");
}

IOxfReactive::TakeEventStatus Abfuellstation::state_5_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_5_active) {
        // State Offen
        case Offen:
        {
            res = Offen_handleEvent();
        }
        break;
        // State Zu
        case Zu:
        {
            if(IS_EVENT_TYPE_OF(OMTimeoutEventId))
                {
                    if(getCurrentEvent() == state_5_timeout)
                        {
                            NOTIFY_TRANSITION_STARTED("6");
                            popNullTransition();
                            cancel(state_5_timeout);
                            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_5.Zu");
                            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5.Zu");
                            pushNullTransition();
                            state_5_subState = Zu;
                            state_5_active = Zu;
                            state_5_timeout = scheduleTimeout(500, "ROOT.Betrieb.state_5.Zu");
                            NOTIFY_TRANSITION_TERMINATED("6");
                            res = eventConsumed;
                        }
                }
            else if(IS_EVENT_TYPE_OF(OMNullEventId))
                {
                    //## transition 8 
                    if(!itsTuer.getZustand())
                        {
                            NOTIFY_TRANSITION_STARTED("8");
                            popNullTransition();
                            cancel(state_5_timeout);
                            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_5.Zu");
                            //#[ transition 8 
                            GEN(evStop);
                            //#]
                            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5.Offen");
                            pushNullTransition();
                            state_5_subState = Offen;
                            state_5_active = Offen;
                            state_5_timeout = scheduleTimeout(500, "ROOT.Betrieb.state_5.Offen");
                            NOTIFY_TRANSITION_TERMINATED("8");
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

IOxfReactive::TakeEventStatus Abfuellstation::Offen_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(evFuellen_System_id))
        {
            NOTIFY_TRANSITION_STARTED("12");
            //#[ transition 12 
            fuellen();
            //#]
            NOTIFY_TRANSITION_TERMINATED("12");
            res = eventConsumed;
        }
    else if(IS_EVENT_TYPE_OF(evNoGlas_System_id))
        {
            NOTIFY_TRANSITION_STARTED("11");
            //#[ transition 11 
            getGlas();
            //#]
            NOTIFY_TRANSITION_TERMINATED("11");
            res = eventConsumed;
        }
    else if(IS_EVENT_TYPE_OF(OMTimeoutEventId))
        {
            if(getCurrentEvent() == state_5_timeout)
                {
                    NOTIFY_TRANSITION_STARTED("5");
                    popNullTransition();
                    cancel(state_5_timeout);
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_5.Offen");
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5.Offen");
                    pushNullTransition();
                    state_5_subState = Offen;
                    state_5_active = Offen;
                    state_5_timeout = scheduleTimeout(500, "ROOT.Betrieb.state_5.Offen");
                    NOTIFY_TRANSITION_TERMINATED("5");
                    res = eventConsumed;
                }
        }
    else if(IS_EVENT_TYPE_OF(OMNullEventId))
        {
            //## transition 7 
            if(itsTuer.getZustand())
                {
                    NOTIFY_TRANSITION_STARTED("7");
                    popNullTransition();
                    cancel(state_5_timeout);
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_5.Offen");
                    //#[ transition 7 
                     GEN(evContinue);
                    //#]
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5.Zu");
                    pushNullTransition();
                    state_5_subState = Zu;
                    state_5_active = Zu;
                    state_5_timeout = scheduleTimeout(500, "ROOT.Betrieb.state_5.Zu");
                    NOTIFY_TRANSITION_TERMINATED("7");
                    res = eventConsumed;
                }
        }
    
    
    return res;
}

void Abfuellstation::state_4_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4");
    NOTIFY_TRANSITION_STARTED("0");
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Idle");
    state_4_subState = Idle;
    state_4_active = Idle;
    NOTIFY_TRANSITION_TERMINATED("0");
}

IOxfReactive::TakeEventStatus Abfuellstation::state_4_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_4_active) {
        // State Idle
        case Idle:
        {
            if(IS_EVENT_TYPE_OF(evRun_System_id))
                {
                    //## transition 1 
                    if(checkGlas())
                        {
                            NOTIFY_TRANSITION_STARTED("1");
                            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Idle");
                            //#[ transition 1 
                            setTara();
                            //#]
                            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running");
                            pushNullTransition();
                            state_4_subState = Running;
                            state_4_active = Running;
                            //#[ state Betrieb.state_4.Running.(Entry) 
                            
                            itsDosierer.GEN(evRun);
                            //#]
                            state_4_timeout = scheduleTimeout(MaxTime, "ROOT.Betrieb.state_4.Running");
                            NOTIFY_TRANSITION_TERMINATED("1");
                            res = eventConsumed;
                        }
                }
            
            
        }
        break;
        // State Running
        case Running:
        {
            res = Running_handleEvent();
        }
        break;
        // State Stopped
        case Stopped:
        {
            if(IS_EVENT_TYPE_OF(evContinue_System_id))
                {
                    //## transition 15 
                    if(checkGlas())
                        {
                            NOTIFY_TRANSITION_STARTED("3");
                            NOTIFY_TRANSITION_STARTED("15");
                            //#[ state Betrieb.state_4.Stopped.(Exit) 
                            Error = false;
                            //#]
                            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Stopped");
                            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running");
                            pushNullTransition();
                            state_4_subState = Running;
                            state_4_active = Running;
                            //#[ state Betrieb.state_4.Running.(Entry) 
                            
                            itsDosierer.GEN(evRun);
                            //#]
                            state_4_timeout = scheduleTimeout(MaxTime, "ROOT.Betrieb.state_4.Running");
                            NOTIFY_TRANSITION_TERMINATED("15");
                            NOTIFY_TRANSITION_TERMINATED("3");
                            res = eventConsumed;
                        }
                    else
                        {
                            NOTIFY_TRANSITION_STARTED("3");
                            NOTIFY_TRANSITION_STARTED("14");
                            //#[ state Betrieb.state_4.Stopped.(Exit) 
                            Error = false;
                            //#]
                            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Stopped");
                            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Idle");
                            state_4_subState = Idle;
                            state_4_active = Idle;
                            NOTIFY_TRANSITION_TERMINATED("14");
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

IOxfReactive::TakeEventStatus Abfuellstation::Running_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(evStop_System_id))
        {
            NOTIFY_TRANSITION_STARTED("2");
            popNullTransition();
            cancel(state_4_timeout);
            //#[ state Betrieb.state_4.Running.(Exit) 
            itsDosierer.GEN(evStop);
            //#]
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running");
            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Stopped");
            state_4_subState = Stopped;
            state_4_active = Stopped;
            //#[ state Betrieb.state_4.Stopped.(Entry) 
            Error = true;
            //#]
            NOTIFY_TRANSITION_TERMINATED("2");
            res = eventConsumed;
        }
    else if(IS_EVENT_TYPE_OF(OMTimeoutEventId))
        {
            if(getCurrentEvent() == state_4_timeout)
                {
                    NOTIFY_TRANSITION_STARTED("13");
                    popNullTransition();
                    cancel(state_4_timeout);
                    //#[ state Betrieb.state_4.Running.(Exit) 
                    itsDosierer.GEN(evStop);
                    //#]
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running");
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Stopped");
                    state_4_subState = Stopped;
                    state_4_active = Stopped;
                    //#[ state Betrieb.state_4.Stopped.(Entry) 
                    Error = true;
                    //#]
                    NOTIFY_TRANSITION_TERMINATED("13");
                    res = eventConsumed;
                }
        }
    else if(IS_EVENT_TYPE_OF(OMNullEventId))
        {
            NOTIFY_TRANSITION_STARTED("4");
            popNullTransition();
            cancel(state_4_timeout);
            //#[ state Betrieb.state_4.Running.(Exit) 
            itsDosierer.GEN(evStop);
            //#]
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running");
            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Idle");
            state_4_subState = Idle;
            state_4_active = Idle;
            NOTIFY_TRANSITION_TERMINATED("4");
            res = eventConsumed;
        }
    
    
    return res;
}

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedAbfuellstation::serializeAttributes(AOMSAttributes* aomsAttributes) const {
    OMAnimatedStation::serializeAttributes(aomsAttributes);
}

void OMAnimatedAbfuellstation::serializeRelations(AOMSRelations* aomsRelations) const {
    aomsRelations->addRelation("itsDosierer", true, true);
    aomsRelations->ADD_ITEM(&myReal->itsDosierer);
    aomsRelations->addRelation("itsVorrat", true, true);
    aomsRelations->ADD_ITEM(&myReal->itsVorrat);
    OMAnimatedStation::serializeRelations(aomsRelations);
}

void OMAnimatedAbfuellstation::rootState_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT");
    if(myReal->rootState_subState == Abfuellstation::Betrieb)
        {
            Betrieb_serializeStates(aomsState);
        }
}

void OMAnimatedAbfuellstation::Betrieb_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb");
    state_4_serializeStates(aomsState);
    state_5_serializeStates(aomsState);
}

void OMAnimatedAbfuellstation::state_5_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_5");
    switch (myReal->state_5_subState) {
        case Abfuellstation::Offen:
        {
            Offen_serializeStates(aomsState);
        }
        break;
        case Abfuellstation::Zu:
        {
            Zu_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedAbfuellstation::Zu_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_5.Zu");
}

void OMAnimatedAbfuellstation::Offen_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_5.Offen");
}

void OMAnimatedAbfuellstation::state_4_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4");
    switch (myReal->state_4_subState) {
        case Abfuellstation::Idle:
        {
            Idle_serializeStates(aomsState);
        }
        break;
        case Abfuellstation::Running:
        {
            Running_serializeStates(aomsState);
        }
        break;
        case Abfuellstation::Stopped:
        {
            Stopped_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedAbfuellstation::Stopped_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Stopped");
}

void OMAnimatedAbfuellstation::Running_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running");
}

void OMAnimatedAbfuellstation::Idle_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Idle");
}
//#]

IMPLEMENT_REACTIVE_META_S_P(Abfuellstation, System, false, Station, OMAnimatedStation, OMAnimatedAbfuellstation)

OMINIT_SUPERCLASS(Station, OMAnimatedStation)

OMREGISTER_REACTIVE_CLASS
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: Systemkomponente/Simulation/Abfuellstation.cpp
*********************************************************************/
