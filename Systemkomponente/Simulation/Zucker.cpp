/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Zucker
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Zucker.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX

#define _OMSTATECHART_ANIMATED
//#]

//## auto_generated
#include "Zucker.h"
//## auto_generated
#include "Karussell.h"
//## auto_generated
#include "Kolben.h"
//## auto_generated
#include "Waage.h"
//#[ ignore
#define System_Zucker_Zucker_SERIALIZE OM_NO_OP
//#]

//## package System

//## class Zucker
Zucker::Zucker(IOxfActive* theActiveContext) {
    NOTIFY_REACTIVE_CONSTRUCTOR(Zucker, Zucker(), 0, System_Zucker_Zucker_SERIALIZE);
    setActiveContext(theActiveContext, false);
    initStatechart();
}

Zucker::~Zucker() {
    NOTIFY_DESTRUCTOR(~Zucker, false);
    cancelTimeouts();
}

bool Zucker::startBehavior() {
    bool done = false;
    done = Abfuellstation::startBehavior();
    return done;
}

void Zucker::initStatechart() {
    rootState_subState = OMNonState;
    rootState_active = OMNonState;
    state_5_subState = OMNonState;
    state_5_active = OMNonState;
    state_4_subState = OMNonState;
    state_4_active = OMNonState;
    Running_subState = OMNonState;
    Running_timeout = NULL;
}

void Zucker::cancelTimeouts() {
    cancel(Running_timeout);
}

bool Zucker::cancelTimeout(const IOxfTimeout* arg) {
    bool res = false;
    res = Abfuellstation::cancelTimeout(arg);
    if(Running_timeout == arg)
        {
            Running_timeout = NULL;
            res = true;
        }
    return res;
}

void Zucker::rootState_entDef() {
    {
        NOTIFY_STATE_ENTERED("ROOT");
        NOTIFY_TRANSITION_STARTED("9");
        Betrieb_entDef();
        NOTIFY_TRANSITION_TERMINATED("9");
    }
}

IOxfReactive::TakeEventStatus Zucker::rootState_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    // State Betrieb
    if(rootState_active == Betrieb)
        {
            res = Betrieb_processEvent();
        }
    return res;
}

void Zucker::Betrieb_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb");
    rootState_subState = Betrieb;
    rootState_active = Betrieb;
    state_4_entDef();
    state_5_entDef();
}

void Zucker::Betrieb_exit() {
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
            Running_exit();
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

IOxfReactive::TakeEventStatus Zucker::Betrieb_processEvent() {
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

void Zucker::state_5_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5");
    NOTIFY_TRANSITION_STARTED("10");
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5.Offen");
    pushNullTransition();
    state_5_subState = Offen;
    state_5_active = Offen;
    state_5_timeout = scheduleTimeout(500, "ROOT.Betrieb.state_5.Offen");
    NOTIFY_TRANSITION_TERMINATED("10");
}

IOxfReactive::TakeEventStatus Zucker::state_5_processEvent() {
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

IOxfReactive::TakeEventStatus Zucker::Offen_handleEvent() {
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

void Zucker::state_4_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4");
    NOTIFY_TRANSITION_STARTED("0");
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Idle");
    state_4_subState = Idle;
    state_4_active = Idle;
    NOTIFY_TRANSITION_TERMINATED("0");
}

IOxfReactive::TakeEventStatus Zucker::state_4_processEvent() {
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
                            Running_entDef();
                            NOTIFY_TRANSITION_TERMINATED("1");
                            res = eventConsumed;
                        }
                }
            
            
        }
        break;
        // State dosieren
        case dosieren:
        {
            res = dosieren_handleEvent();
        }
        break;
        // State terminationstate_9
        case terminationstate_9:
        {
            res = terminationstate_9_handleEvent();
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
                            Running_entDef();
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

void Zucker::Running_exit() {
    popNullTransition();
    switch (Running_subState) {
        // State dosieren
        case dosieren:
        {
            popNullTransition();
            cancel(Running_timeout);
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.dosieren");
        }
        break;
        // State terminationstate_9
        case terminationstate_9:
        {
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.terminationstate_9");
        }
        break;
        default:
            break;
    }
    Running_subState = OMNonState;
    cancel(state_4_timeout);
    //#[ state Betrieb.state_4.Running.(Exit) 
    itsDosierer.GEN(evStop);
    //#]
    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running");
}

void Zucker::Running_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running");
    pushNullTransition();
    state_4_subState = Running;
    //#[ state Betrieb.state_4.Running.(Entry) 
    
    itsDosierer.GEN(evRun);
    //#]
    state_4_timeout = scheduleTimeout(MaxTime, "ROOT.Betrieb.state_4.Running");
    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.0");
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.dosieren");
    pushNullTransition();
    Running_subState = dosieren;
    state_4_active = dosieren;
    Running_timeout = scheduleTimeout(500, "ROOT.Betrieb.state_4.Running.ROOT.Running.dosieren");
    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.0");
}

IOxfReactive::TakeEventStatus Zucker::Running_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(evStop_System_id))
        {
            NOTIFY_TRANSITION_STARTED("2");
            Running_exit();
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
                    Running_exit();
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
            //## transition 4 
            if(IS_COMPLETED(Running)==true)
                {
                    NOTIFY_TRANSITION_STARTED("4");
                    Running_exit();
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Idle");
                    state_4_subState = Idle;
                    state_4_active = Idle;
                    NOTIFY_TRANSITION_TERMINATED("4");
                    res = eventConsumed;
                }
        }
    
    
    return res;
}

IOxfReactive::TakeEventStatus Zucker::terminationstate_9_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    res = Running_handleEvent();
    return res;
}

IOxfReactive::TakeEventStatus Zucker::dosieren_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(OMTimeoutEventId))
        {
            if(getCurrentEvent() == Running_timeout)
                {
                    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.1");
                    popNullTransition();
                    cancel(Running_timeout);
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.dosieren");
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.dosieren");
                    pushNullTransition();
                    Running_subState = dosieren;
                    state_4_active = dosieren;
                    Running_timeout = scheduleTimeout(500, "ROOT.Betrieb.state_4.Running.ROOT.Running.dosieren");
                    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.1");
                    res = eventConsumed;
                }
        }
    else if(IS_EVENT_TYPE_OF(OMNullEventId))
        {
            //## transition Betrieb.state_4.Running.2 
            if(getDosierMenge() <= getNetto())
                {
                    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.2");
                    popNullTransition();
                    cancel(Running_timeout);
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.dosieren");
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.terminationstate_9");
                    Running_subState = terminationstate_9;
                    state_4_active = terminationstate_9;
                    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.2");
                    res = eventConsumed;
                }
        }
    
    if(res == eventNotConsumed)
        {
            res = Running_handleEvent();
        }
    return res;
}

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedZucker::serializeAttributes(AOMSAttributes* aomsAttributes) const {
    OMAnimatedAbfuellstation::serializeAttributes(aomsAttributes);
}

void OMAnimatedZucker::serializeRelations(AOMSRelations* aomsRelations) const {
    OMAnimatedAbfuellstation::serializeRelations(aomsRelations);
}

void OMAnimatedZucker::rootState_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT");
    if(myReal->rootState_subState == Zucker::Betrieb)
        {
            Betrieb_serializeStates(aomsState);
        }
}

void OMAnimatedZucker::Betrieb_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb");
    state_4_serializeStates(aomsState);
    state_5_serializeStates(aomsState);
}

void OMAnimatedZucker::state_5_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_5");
    switch (myReal->state_5_subState) {
        case Zucker::Offen:
        {
            Offen_serializeStates(aomsState);
        }
        break;
        case Zucker::Zu:
        {
            Zu_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedZucker::Zu_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_5.Zu");
}

void OMAnimatedZucker::Offen_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_5.Offen");
}

void OMAnimatedZucker::state_4_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4");
    switch (myReal->state_4_subState) {
        case Zucker::Idle:
        {
            Idle_serializeStates(aomsState);
        }
        break;
        case Zucker::Running:
        {
            Running_serializeStates(aomsState);
        }
        break;
        case Zucker::Stopped:
        {
            Stopped_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedZucker::Stopped_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Stopped");
}

void OMAnimatedZucker::Running_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running");
    switch (myReal->Running_subState) {
        case Zucker::dosieren:
        {
            dosieren_serializeStates(aomsState);
        }
        break;
        case Zucker::terminationstate_9:
        {
            terminationstate_9_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedZucker::terminationstate_9_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.terminationstate_9");
}

void OMAnimatedZucker::dosieren_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.dosieren");
}

void OMAnimatedZucker::Idle_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Idle");
}
//#]

IMPLEMENT_REACTIVE_META_S_P(Zucker, System, false, Abfuellstation, OMAnimatedAbfuellstation, OMAnimatedZucker)

OMINIT_SUPERCLASS(Abfuellstation, OMAnimatedAbfuellstation)

OMREGISTER_REACTIVE_CLASS
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: Systemkomponente/Simulation/Zucker.cpp
*********************************************************************/
