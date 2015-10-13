/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Stampfer
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Stampfer.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX

#define _OMSTATECHART_ANIMATED
//#]

//## auto_generated
#include "Stampfer.h"
//## auto_generated
#include "Karussell.h"
//## auto_generated
#include "Waage.h"
//#[ ignore
#define System_Stampfer_Stampfer_SERIALIZE OM_NO_OP
//#]

//## package System

//## class Stampfer
Stampfer::Stampfer(IOxfActive* theActiveContext) : runde(1) {
    NOTIFY_REACTIVE_CONSTRUCTOR(Stampfer, Stampfer(), 0, System_Stampfer_Stampfer_SERIALIZE);
    setActiveContext(theActiveContext, false);
    {
        {
            itsStampferkolben.setShouldDelete(false);
        }
    }
    initStatechart();
    //#[ operation Stampfer()
    itsStampferkolben.setItsStation(this);
    //#]
}

Stampfer::~Stampfer() {
    NOTIFY_DESTRUCTOR(~Stampfer, false);
}

int Stampfer::getRunde() const {
    return runde;
}

void Stampfer::setRunde(int p_runde) {
    runde = p_runde;
}

Kolben* Stampfer::getItsStampferkolben() const {
    return (Kolben*) &itsStampferkolben;
}

bool Stampfer::startBehavior() {
    bool done = true;
    done &= Station::startBehavior();
    done &= itsStampferkolben.startBehavior();
    return done;
}

void Stampfer::initStatechart() {
    rootState_subState = OMNonState;
    rootState_active = OMNonState;
    state_5_subState = OMNonState;
    state_5_active = OMNonState;
    state_4_subState = OMNonState;
    state_4_active = OMNonState;
    Running_subState = OMNonState;
}

void Stampfer::setActiveContext(IOxfActive* theActiveContext, bool activeInstance) {
    OMReactive::setActiveContext(theActiveContext, activeInstance);
    {
        itsStampferkolben.setActiveContext(theActiveContext, false);
    }
}

void Stampfer::destroy() {
    itsStampferkolben.destroy();
    Station::destroy();
}

void Stampfer::rootState_entDef() {
    {
        NOTIFY_STATE_ENTERED("ROOT");
        NOTIFY_TRANSITION_STARTED("9");
        Betrieb_entDef();
        NOTIFY_TRANSITION_TERMINATED("9");
    }
}

IOxfReactive::TakeEventStatus Stampfer::rootState_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    // State Betrieb
    if(rootState_active == Betrieb)
        {
            res = Betrieb_processEvent();
        }
    return res;
}

void Stampfer::Betrieb_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb");
    rootState_subState = Betrieb;
    rootState_active = Betrieb;
    state_4_entDef();
    state_5_entDef();
}

void Stampfer::Betrieb_exit() {
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

IOxfReactive::TakeEventStatus Stampfer::Betrieb_processEvent() {
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

void Stampfer::state_5_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5");
    NOTIFY_TRANSITION_STARTED("10");
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5.Offen");
    pushNullTransition();
    state_5_subState = Offen;
    state_5_active = Offen;
    state_5_timeout = scheduleTimeout(500, "ROOT.Betrieb.state_5.Offen");
    NOTIFY_TRANSITION_TERMINATED("10");
}

IOxfReactive::TakeEventStatus Stampfer::state_5_processEvent() {
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

IOxfReactive::TakeEventStatus Stampfer::Offen_handleEvent() {
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

void Stampfer::state_4_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4");
    NOTIFY_TRANSITION_STARTED("0");
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Idle");
    state_4_subState = Idle;
    state_4_active = Idle;
    NOTIFY_TRANSITION_TERMINATED("0");
}

IOxfReactive::TakeEventStatus Stampfer::state_4_processEvent() {
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
                            runde = 1;
                            //#]
                            Running_entDef();
                            NOTIFY_TRANSITION_TERMINATED("1");
                            res = eventConsumed;
                        }
                }
            
            
        }
        break;
        // State terminationstate_22
        case terminationstate_22:
        {
            res = terminationstate_22_handleEvent();
        }
        break;
        // State Up
        case Up:
        {
            res = Up_handleEvent();
        }
        break;
        // State Down
        case Down:
        {
            res = Down_handleEvent();
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

void Stampfer::Running_exit() {
    popNullTransition();
    switch (Running_subState) {
        // State terminationstate_22
        case terminationstate_22:
        {
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.terminationstate_22");
        }
        break;
        // State Up
        case Up:
        {
            //#[ state Betrieb.state_4.Running.Running.Up.(Exit) 
            //itsStampferkolben.GEN(evStop);
            //#]
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Up");
        }
        break;
        // State Down
        case Down:
        {
            //#[ state Betrieb.state_4.Running.Running.Down.(Exit) 
              //itsStampferkolben.GEN(evStop());
              ++runde;
            //#]
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Down");
        }
        break;
        default:
            break;
    }
    Running_subState = OMNonState;
    cancel(state_4_timeout);
    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running");
}

void Stampfer::Running_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running");
    pushNullTransition();
    state_4_subState = Running;
    state_4_timeout = scheduleTimeout(MaxTime, "ROOT.Betrieb.state_4.Running");
    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.1");
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Down");
    Running_subState = Down;
    state_4_active = Down;
    //#[ state Betrieb.state_4.Running.Running.Down.(Entry) 
    itsStampferkolben.setDown(true); 
    itsStampferkolben.GEN(evRun());
    //#]
    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.1");
}

IOxfReactive::TakeEventStatus Stampfer::Running_handleEvent() {
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
            itsStampferkolben.setDown(false); 
            itsStampferkolben.GEN(evRun);
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
                    itsStampferkolben.setDown(false); 
                    itsStampferkolben.GEN(evRun);
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

IOxfReactive::TakeEventStatus Stampfer::Up_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(evReady_System_id))
        {
            //## transition Betrieb.state_4.Running.4 
            if(runde<4)
                {
                    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.2");
                    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.4");
                    //#[ state Betrieb.state_4.Running.Running.Up.(Exit) 
                    //itsStampferkolben.GEN(evStop);
                    //#]
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Up");
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Down");
                    Running_subState = Down;
                    state_4_active = Down;
                    //#[ state Betrieb.state_4.Running.Running.Down.(Entry) 
                    itsStampferkolben.setDown(true); 
                    itsStampferkolben.GEN(evRun());
                    //#]
                    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.4");
                    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.2");
                    res = eventConsumed;
                }
            else
                {
                    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.2");
                    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.0");
                    //#[ state Betrieb.state_4.Running.Running.Up.(Exit) 
                    //itsStampferkolben.GEN(evStop);
                    //#]
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Up");
                    //#[ transition Betrieb.state_4.Running.0 
                    runde=1;
                    //#]
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.terminationstate_22");
                    Running_subState = terminationstate_22;
                    state_4_active = terminationstate_22;
                    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.0");
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

IOxfReactive::TakeEventStatus Stampfer::terminationstate_22_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    res = Running_handleEvent();
    return res;
}

IOxfReactive::TakeEventStatus Stampfer::Down_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(evReady_System_id))
        {
            NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.3");
            //#[ state Betrieb.state_4.Running.Running.Down.(Exit) 
              //itsStampferkolben.GEN(evStop());
              ++runde;
            //#]
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Down");
            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Up");
            Running_subState = Up;
            state_4_active = Up;
            //#[ state Betrieb.state_4.Running.Running.Up.(Entry) 
            itsStampferkolben.setDown(false); 
            itsStampferkolben.GEN(evRun);
            //#]
            NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.3");
            res = eventConsumed;
        }
    
    if(res == eventNotConsumed)
        {
            res = Running_handleEvent();
        }
    return res;
}

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedStampfer::serializeAttributes(AOMSAttributes* aomsAttributes) const {
    aomsAttributes->addAttribute("runde", x2String(myReal->runde));
    OMAnimatedStation::serializeAttributes(aomsAttributes);
}

void OMAnimatedStampfer::serializeRelations(AOMSRelations* aomsRelations) const {
    aomsRelations->addRelation("itsStampferkolben", true, true);
    aomsRelations->ADD_ITEM(&myReal->itsStampferkolben);
    OMAnimatedStation::serializeRelations(aomsRelations);
}

void OMAnimatedStampfer::rootState_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT");
    if(myReal->rootState_subState == Stampfer::Betrieb)
        {
            Betrieb_serializeStates(aomsState);
        }
}

void OMAnimatedStampfer::Betrieb_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb");
    state_4_serializeStates(aomsState);
    state_5_serializeStates(aomsState);
}

void OMAnimatedStampfer::state_5_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_5");
    switch (myReal->state_5_subState) {
        case Stampfer::Offen:
        {
            Offen_serializeStates(aomsState);
        }
        break;
        case Stampfer::Zu:
        {
            Zu_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedStampfer::Zu_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_5.Zu");
}

void OMAnimatedStampfer::Offen_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_5.Offen");
}

void OMAnimatedStampfer::state_4_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4");
    switch (myReal->state_4_subState) {
        case Stampfer::Idle:
        {
            Idle_serializeStates(aomsState);
        }
        break;
        case Stampfer::Running:
        {
            Running_serializeStates(aomsState);
        }
        break;
        case Stampfer::Stopped:
        {
            Stopped_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedStampfer::Stopped_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Stopped");
}

void OMAnimatedStampfer::Running_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running");
    switch (myReal->Running_subState) {
        case Stampfer::terminationstate_22:
        {
            terminationstate_22_serializeStates(aomsState);
        }
        break;
        case Stampfer::Up:
        {
            Up_serializeStates(aomsState);
        }
        break;
        case Stampfer::Down:
        {
            Down_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedStampfer::Up_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.Up");
}

void OMAnimatedStampfer::terminationstate_22_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.terminationstate_22");
}

void OMAnimatedStampfer::Down_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.Down");
}

void OMAnimatedStampfer::Idle_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Idle");
}
//#]

IMPLEMENT_REACTIVE_META_S_P(Stampfer, System, false, Station, OMAnimatedStation, OMAnimatedStampfer)

OMINIT_SUPERCLASS(Station, OMAnimatedStation)

OMREGISTER_REACTIVE_CLASS
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: Systemkomponente/Simulation/Stampfer.cpp
*********************************************************************/
