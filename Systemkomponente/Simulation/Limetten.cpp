/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Limetten
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Limetten.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX

#define _OMSTATECHART_ANIMATED
//#]

//## auto_generated
#include "Limetten.h"
//## auto_generated
#include "Karussell.h"
//## link itsLichtschranke
#include "Lichtschranke.h"
//## auto_generated
#include "Waage.h"
//#[ ignore
#define System_Limetten_Limetten_SERIALIZE OM_NO_OP

#define System_Limetten_evLIMReady_SERIALIZE OM_NO_OP

#define System_Limetten_noLimette_SERIALIZE OM_NO_OP
//#]

//## package System

//## class Limetten
Limetten::Limetten(IOxfActive* theActiveContext) : TheLimette(false) {
    NOTIFY_REACTIVE_CONSTRUCTOR(Limetten, Limetten(), 0, System_Limetten_Limetten_SERIALIZE);
    setActiveContext(theActiveContext, false);
    {
        {
            itsSchneider.setShouldDelete(false);
        }
        {
            itsSchieber.setShouldDelete(false);
        }
    }
    itsLichtschranke = NULL;
    initStatechart();
    //#[ operation Limetten()
    itsSchieber.setItsStation(this); 
    itsSchneider.setItsStation(this);
    setDosierMenge(80);
    itsVorrat.setMaxVorrat(1);
    itsVorrat.setVorhandenerVorrat(60);
    
    //#]
}

Limetten::~Limetten() {
    NOTIFY_DESTRUCTOR(~Limetten, false);
    cleanUpRelations();
    cancelTimeouts();
}

void Limetten::noLimette() {
    NOTIFY_OPERATION(noLimette, noLimette(), 0, System_Limetten_noLimette_SERIALIZE);
    //#[ operation noLimette()
    TheLimette = false;
    //#]
}

bool Limetten::getTheLimette() const {
    return TheLimette;
}

void Limetten::setTheLimette(bool p_TheLimette) {
    TheLimette = p_TheLimette;
    NOTIFY_SET_OPERATION;
}

Lichtschranke* Limetten::getItsLichtschranke() const {
    return itsLichtschranke;
}

void Limetten::setItsLichtschranke(Lichtschranke* p_Lichtschranke) {
    itsLichtschranke = p_Lichtschranke;
    if(p_Lichtschranke != NULL)
        {
            NOTIFY_RELATION_ITEM_ADDED("itsLichtschranke", p_Lichtschranke, false, true);
        }
    else
        {
            NOTIFY_RELATION_CLEARED("itsLichtschranke");
        }
}

Kolben* Limetten::getItsSchieber() const {
    return (Kolben*) &itsSchieber;
}

Limettenschneider* Limetten::getItsSchneider() const {
    return (Limettenschneider*) &itsSchneider;
}

bool Limetten::startBehavior() {
    bool done = true;
    done &= Abfuellstation::startBehavior();
    done &= itsSchieber.startBehavior();
    done &= itsSchneider.startBehavior();
    return done;
}

void Limetten::initStatechart() {
    rootState_subState = OMNonState;
    rootState_active = OMNonState;
    state_5_subState = OMNonState;
    state_5_active = OMNonState;
    state_4_subState = OMNonState;
    state_4_active = OMNonState;
    Running_subState = OMNonState;
    Running_lastState = OMNonState;
    state_48_subState = OMNonState;
    state_48_active = OMNonState;
    state_47_subState = OMNonState;
    state_47_active = OMNonState;
    Reset_state_48_subState = OMNonState;
    Reset_state_48_active = OMNonState;
    Reset_state_47_subState = OMNonState;
    Reset_state_47_active = OMNonState;
    Idle_subState = OMNonState;
    Idle_timeout = NULL;
}

void Limetten::cleanUpRelations() {
    if(itsLichtschranke != NULL)
        {
            NOTIFY_RELATION_CLEARED("itsLichtschranke");
            itsLichtschranke = NULL;
        }
}

void Limetten::cancelTimeouts() {
    cancel(Idle_timeout);
}

bool Limetten::cancelTimeout(const IOxfTimeout* arg) {
    bool res = false;
    res = Abfuellstation::cancelTimeout(arg);
    if(Idle_timeout == arg)
        {
            Idle_timeout = NULL;
            res = true;
        }
    return res;
}

//#[ ignore
#undef OM_RET_TYPE
#define OM_RET_TYPE 
#undef OM_SER_RET
#define OM_SER_RET(val) 
#undef OM_SER_OUT
#define OM_SER_OUT 
//#]


void Limetten::evLIMReady() {
    NOTIFY_TRIGGERED_OPERATION(evLIMReady, evLIMReady(), 0, System_Limetten_evLIMReady_SERIALIZE);
    evLIMReady_Limetten_Event triggerEvent;
    handleTrigger(&triggerEvent);
    OM_RETURN_VOID;
}

void Limetten::setActiveContext(IOxfActive* theActiveContext, bool activeInstance) {
    OMReactive::setActiveContext(theActiveContext, activeInstance);
    {
        itsSchneider.setActiveContext(theActiveContext, false);
        itsSchieber.setActiveContext(theActiveContext, false);
    }
}

void Limetten::destroy() {
    itsSchieber.destroy();
    itsSchneider.destroy();
    Abfuellstation::destroy();
}

void Limetten::rootState_entDef() {
    {
        NOTIFY_STATE_ENTERED("ROOT");
        NOTIFY_TRANSITION_STARTED("9");
        Betrieb_entDef();
        NOTIFY_TRANSITION_TERMINATED("9");
    }
}

IOxfReactive::TakeEventStatus Limetten::rootState_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    // State Betrieb
    if(rootState_active == Betrieb)
        {
            res = Betrieb_processEvent();
        }
    return res;
}

void Limetten::Betrieb_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb");
    rootState_subState = Betrieb;
    rootState_active = Betrieb;
    state_4_entDef();
    state_5_entDef();
}

void Limetten::Betrieb_exit() {
    state_4_exit();
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

IOxfReactive::TakeEventStatus Limetten::Betrieb_processEvent() {
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

void Limetten::state_5_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5");
    NOTIFY_TRANSITION_STARTED("10");
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5.Offen");
    pushNullTransition();
    state_5_subState = Offen;
    state_5_active = Offen;
    state_5_timeout = scheduleTimeout(500, "ROOT.Betrieb.state_5.Offen");
    NOTIFY_TRANSITION_TERMINATED("10");
}

IOxfReactive::TakeEventStatus Limetten::state_5_processEvent() {
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

IOxfReactive::TakeEventStatus Limetten::Offen_handleEvent() {
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
    else if(IS_EVENT_TYPE_OF(evNoLimette_System_id))
        {
            NOTIFY_TRANSITION_STARTED("19");
            //#[ transition 19 
            noLimette();
            //#]
            NOTIFY_TRANSITION_TERMINATED("19");
            res = eventConsumed;
        }
    
    
    return res;
}

void Limetten::state_4_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4");
    NOTIFY_TRANSITION_STARTED("0");
    Idle_entDef();
    NOTIFY_TRANSITION_TERMINATED("0");
}

void Limetten::state_4_exit() {
    switch (state_4_subState) {
        // State Idle
        case Idle:
        {
            switch (Idle_subState) {
                // State beide_up
                case beide_up:
                {
                    popNullTransition();
                    cancel(Idle_timeout);
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Idle.ROOT.Idle.beide_up");
                }
                break;
                // State terminationstate_33
                case terminationstate_33:
                {
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Idle.ROOT.Idle.terminationstate_33");
                }
                break;
                default:
                    break;
            }
            Idle_subState = OMNonState;
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
        // State Reset
        case state_4_Reset:
        {
            state_4_Reset_exit();
        }
        break;
        default:
            break;
    }
    state_4_subState = OMNonState;
    
    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4");
}

IOxfReactive::TakeEventStatus Limetten::state_4_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_4_active) {
        // State beide_up
        case beide_up:
        {
            res = beide_up_handleEvent();
        }
        break;
        // State terminationstate_33
        case terminationstate_33:
        {
            res = Idle_handleEvent();
        }
        break;
        // State terminationstate_11
        case terminationstate_11:
        {
            res = terminationstate_11_handleEvent();
        }
        break;
        // State Schieben
        case Schieben:
        {
            res = Schieben_handleEvent();
        }
        break;
        // State Check
        case Check:
        {
            res = Check_handleEvent();
        }
        break;
        // State Schneider
        case Schneider:
        {
            res = Schneider_handleEvent();
        }
        break;
        // State Reset
        case Reset:
        {
            res = Reset_processEvent();
        }
        break;
        // State Check_2
        case Check_2:
        {
            res = Check_2_handleEvent();
        }
        break;
        // State ContinueHelperState
        case ContinueHelperState:
        {
            res = ContinueHelperState_handleEvent();
        }
        break;
        // State ContinueHelperState
        case Running_ContinueHelperState:
        {
            res = Running_ContinueHelperState_handleEvent();
        }
        break;
        // State Stopped
        case Stopped:
        {
            res = Stopped_handleEvent();
        }
        break;
        // State Reset
        case state_4_Reset:
        {
            res = state_4_Reset_processEvent();
        }
        break;
        default:
            break;
    }
    return res;
}

IOxfReactive::TakeEventStatus Limetten::StoppedTakeevContinue() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
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
            //#[ state Betrieb.state_4.Running.(Entry) 
            //itsDosierer.GEN(evRun);
            //#]
            state_4_timeout = scheduleTimeout(MaxTime, "ROOT.Betrieb.state_4.Running");
            pushNullTransition();
            Running_subState = Running_ContinueHelperState;
            state_4_active = Running_ContinueHelperState;
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
            state_4_Reset_entDef();
            NOTIFY_TRANSITION_TERMINATED("14");
            NOTIFY_TRANSITION_TERMINATED("3");
            res = eventConsumed;
        }
    return res;
}

IOxfReactive::TakeEventStatus Limetten::Stopped_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(evContinue_System_id))
        {
            res = StoppedTakeevContinue();
        }
    
    
    return res;
}

void Limetten::Running_exit() {
    Running_lastState = Running_subState;
    popNullTransition();
    switch (Running_subState) {
        // State terminationstate_11
        case terminationstate_11:
        {
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.terminationstate_11");
            Running_lastState = terminationstate_11;
        }
        break;
        // State Schieben
        case Schieben:
        {
            //#[ state Betrieb.state_4.Running.Running.Schieben.(Exit) 
            itsSchieber.GEN(evStop());
            //#]
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Schieben");
            Running_lastState = Schieben;
        }
        break;
        // State Check
        case Check:
        {
            popNullTransition();
            //#[ state Betrieb.state_4.Running.Running.Check.(Exit) 
            
            
            //#]
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Check");
            Running_lastState = Check;
        }
        break;
        // State Schneider
        case Schneider:
        {
            //#[ state Betrieb.state_4.Running.Running.Schneider.(Exit) 
            itsSchneider.GEN(evStop());
            //#]
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Schneider");
            Running_lastState = Schneider;
        }
        break;
        // State Reset
        case Reset:
        {
            Reset_exit();
            Running_lastState = Reset;
        }
        break;
        // State Check_2
        case Check_2:
        {
            popNullTransition();
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Check_2");
            Running_lastState = Check_2;
        }
        break;
        // State ContinueHelperState
        case ContinueHelperState:
        {
            popNullTransition();
            Running_lastState = ContinueHelperState;
        }
        break;
        // State ContinueHelperState
        case Running_ContinueHelperState:
        {
            popNullTransition();
            Running_lastState = Running_ContinueHelperState;
        }
        break;
        default:
            break;
    }
    Running_subState = OMNonState;
    cancel(state_4_timeout);
    //#[ state Betrieb.state_4.Running.(Exit) 
    //itsDosierer.GEN(evStop);
    //#]
    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running");
}

void Limetten::Running_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running");
    pushNullTransition();
    state_4_subState = Running;
    //#[ state Betrieb.state_4.Running.(Entry) 
    //itsDosierer.GEN(evRun);
    //#]
    state_4_timeout = scheduleTimeout(MaxTime, "ROOT.Betrieb.state_4.Running");
    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.0");
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Check");
    pushNullTransition();
    Running_subState = Check;
    state_4_active = Check;
    //#[ state Betrieb.state_4.Running.Running.Check.(Entry) 
    TheLimette = false;
    TheLimette = itsLichtschranke->check(); 
    
    //#]
    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.0");
}

void Limetten::Running_entShallowHist() {
    if(Running_lastState != OMNonState)
        {
            Running_subState = Running_lastState;
            switch (Running_subState) {
                // State terminationstate_11
                case terminationstate_11:
                {
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.terminationstate_11");
                    Running_subState = terminationstate_11;
                    state_4_active = terminationstate_11;
                }
                break;
                // State Schieben
                case Schieben:
                {
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Schieben");
                    Running_subState = Schieben;
                    state_4_active = Schieben;
                    //#[ state Betrieb.state_4.Running.Running.Schieben.(Entry) 
                    itsSchieber.setDown(true); 
                    itsSchieber.GEN(evRun());
                    //#]
                }
                break;
                // State Check
                case Check:
                {
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Check");
                    pushNullTransition();
                    Running_subState = Check;
                    state_4_active = Check;
                    //#[ state Betrieb.state_4.Running.Running.Check.(Entry) 
                    TheLimette = false;
                    TheLimette = itsLichtschranke->check(); 
                    
                    //#]
                }
                break;
                // State Schneider
                case Schneider:
                {
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Schneider");
                    Running_subState = Schneider;
                    state_4_active = Schneider;
                    //#[ state Betrieb.state_4.Running.Running.Schneider.(Entry) 
                    itsSchneider.setDown(true); 
                    itsSchneider.GEN(evRun());
                    //#]
                }
                break;
                // State Reset
                case Reset:
                {
                    Reset_entDef();
                }
                break;
                // State Check_2
                case Check_2:
                {
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Check_2");
                    pushNullTransition();
                    Running_subState = Check_2;
                    state_4_active = Check_2;
                }
                break;
                // State ContinueHelperState
                case ContinueHelperState:
                {
                    pushNullTransition();
                    Running_subState = ContinueHelperState;
                    state_4_active = ContinueHelperState;
                }
                break;
                // State ContinueHelperState
                case Running_ContinueHelperState:
                {
                    pushNullTransition();
                    Running_subState = Running_ContinueHelperState;
                    state_4_active = Running_ContinueHelperState;
                }
                break;
                default:
                    break;
            }
        }
}

IOxfReactive::TakeEventStatus Limetten::Running_handleEvent() {
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
                    //#[ transition 4 
                    noLimette();
                    //#]
                    Idle_entDef();
                    NOTIFY_TRANSITION_TERMINATED("4");
                    res = eventConsumed;
                }
        }
    
    
    return res;
}

IOxfReactive::TakeEventStatus Limetten::terminationstate_11_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    res = Running_handleEvent();
    return res;
}

IOxfReactive::TakeEventStatus Limetten::Schneider_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(evSReady_System_id))
        {
            NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.4");
            //#[ state Betrieb.state_4.Running.Running.Schneider.(Exit) 
            itsSchneider.GEN(evStop());
            //#]
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Schneider");
            //#[ transition Betrieb.state_4.Running.4 
            dosiere(100);
            //#]
            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Check_2");
            pushNullTransition();
            Running_subState = Check_2;
            state_4_active = Check_2;
            NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.4");
            res = eventConsumed;
        }
    
    if(res == eventNotConsumed)
        {
            res = Running_handleEvent();
        }
    return res;
}

IOxfReactive::TakeEventStatus Limetten::Schieben_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(evReady_System_id))
        {
            NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.3");
            //#[ state Betrieb.state_4.Running.Running.Schieben.(Exit) 
            itsSchieber.GEN(evStop());
            //#]
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Schieben");
            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Schneider");
            Running_subState = Schneider;
            state_4_active = Schneider;
            //#[ state Betrieb.state_4.Running.Running.Schneider.(Entry) 
            itsSchneider.setDown(true); 
            itsSchneider.GEN(evRun());
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

bool Limetten::Reset_isCompleted() {
    if(IS_COMPLETED(state_47) == false)
        {
            return false;
        }
    if(IS_COMPLETED(state_48) == false)
        {
            return false;
        }
    return true;
}

void Limetten::Reset_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset");
    Running_subState = Reset;
    state_4_active = Reset;
    //#[ state Betrieb.state_4.Running.Running.Reset.(Entry) 
    itsSchneider.setDown(false);
    itsSchieber.setDown(false);  
    itsSchneider.GEN(evRun());      
    itsSchieber.GEN(evRun());
    //#]
    state_47_entDef();
    state_48_entDef();
}

void Limetten::Reset_exit() {
    switch (state_47_subState) {
        // State SchneiderZuruck
        case SchneiderZuruck:
        {
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_47.SchneiderZuruck");
        }
        break;
        // State terminationstate_51
        case terminationstate_51:
        {
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_47.terminationstate_51");
        }
        break;
        default:
            break;
    }
    state_47_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_47");
    switch (state_48_subState) {
        // State SchieberZuruck
        case SchieberZuruck:
        {
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_48.SchieberZuruck");
        }
        break;
        // State terminationstate_52
        case terminationstate_52:
        {
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_48.terminationstate_52");
        }
        break;
        default:
            break;
    }
    state_48_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_48");
    //#[ state Betrieb.state_4.Running.Running.Reset.(Exit) 
    itsSchneider.GEN(evStop()); 
    itsSchieber.GEN(evStop());
    //#]
    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset");
}

IOxfReactive::TakeEventStatus Limetten::Reset_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    // State state_47
    if(state_47_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(Reset))
                {
                    return res;
                }
        }
    // State state_48
    if(state_48_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(Reset))
                {
                    return res;
                }
        }
    if(res == eventNotConsumed)
        {
            res = Reset_handleEvent();
        }
    return res;
}

IOxfReactive::TakeEventStatus Limetten::Reset_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(evReady_System_id))
        {
            NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.5");
            Reset_exit();
            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.terminationstate_11");
            Running_subState = terminationstate_11;
            state_4_active = terminationstate_11;
            NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.5");
            res = eventConsumed;
        }
    
    if(res == eventNotConsumed)
        {
            res = Running_handleEvent();
        }
    return res;
}

void Limetten::state_48_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_48");
    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.1");
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_48.SchieberZuruck");
    state_48_subState = SchieberZuruck;
    state_48_active = SchieberZuruck;
    //#[ state Betrieb.state_4.Running.Running.Reset.Reset.state_48.SchieberZuruck.(Entry) 
    itsSchieber.setDown(false);
      itsSchieber.GEN(evRun());
    //#]
    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.1");
}

IOxfReactive::TakeEventStatus Limetten::state_48_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_48_active) {
        // State SchieberZuruck
        case SchieberZuruck:
        {
            if(IS_EVENT_TYPE_OF(evReady_System_id))
                {
                    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.2");
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_48.SchieberZuruck");
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_48.terminationstate_52");
                    state_48_subState = terminationstate_52;
                    state_48_active = terminationstate_52;
                    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.2");
                    res = eventConsumed;
                }
            
            
        }
        break;
        
        default:
            break;
    }
    return res;
}

void Limetten::state_47_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_47");
    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.0");
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_47.SchneiderZuruck");
    state_47_subState = SchneiderZuruck;
    state_47_active = SchneiderZuruck;
    //#[ state Betrieb.state_4.Running.Running.Reset.Reset.state_47.SchneiderZuruck.(Entry) 
    itsSchneider.setDown(false); 
    itsSchneider.GEN(evRun()); 
    //#]
    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.0");
}

IOxfReactive::TakeEventStatus Limetten::state_47_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_47_active) {
        // State SchneiderZuruck
        case SchneiderZuruck:
        {
            if(IS_EVENT_TYPE_OF(evReady_System_id))
                {
                    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.3");
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_47.SchneiderZuruck");
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_47.terminationstate_51");
                    state_47_subState = terminationstate_51;
                    state_47_active = terminationstate_51;
                    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.3");
                    res = eventConsumed;
                }
            
            
        }
        break;
        
        default:
            break;
    }
    return res;
}

IOxfReactive::TakeEventStatus Limetten::Running_ContinueHelperState_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(OMNullEventId))
        {
            NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.7");
            popNullTransition();
            pushNullTransition();
            Running_subState = ContinueHelperState;
            state_4_active = ContinueHelperState;
            NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.7");
            res = eventConsumed;
        }
    
    if(res == eventNotConsumed)
        {
            res = Running_handleEvent();
        }
    return res;
}

IOxfReactive::TakeEventStatus Limetten::ContinueHelperState_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(OMNullEventId))
        {
            NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.2");
            Running_entShallowHist();
            NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.2");
            res = eventConsumed;
        }
    
    if(res == eventNotConsumed)
        {
            res = Running_handleEvent();
        }
    return res;
}

IOxfReactive::TakeEventStatus Limetten::Check_2_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(OMNullEventId))
        {
            //## transition Betrieb.state_4.Running.6 
            if(itsKarussell->getBrutto(StationsNr) > 200)
                {
                    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.6");
                    popNullTransition();
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Check_2");
                    Reset_entDef();
                    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.6");
                    res = eventConsumed;
                }
        }
    
    if(res == eventNotConsumed)
        {
            res = Running_handleEvent();
        }
    return res;
}

IOxfReactive::TakeEventStatus Limetten::Check_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(OMNullEventId))
        {
            //## transition Betrieb.state_4.Running.1 
            if(TheLimette == true)
                {
                    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Running.1");
                    popNullTransition();
                    //#[ state Betrieb.state_4.Running.Running.Check.(Exit) 
                    
                    
                    //#]
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running.ROOT.Running.Check");
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running.ROOT.Running.Schieben");
                    Running_subState = Schieben;
                    state_4_active = Schieben;
                    //#[ state Betrieb.state_4.Running.Running.Schieben.(Entry) 
                    itsSchieber.setDown(true); 
                    itsSchieber.GEN(evRun());
                    //#]
                    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Running.1");
                    res = eventConsumed;
                }
        }
    
    if(res == eventNotConsumed)
        {
            res = Running_handleEvent();
        }
    return res;
}

bool Limetten::state_4_Reset_isCompleted() {
    if(IS_COMPLETED(Reset_state_47) == false)
        {
            return false;
        }
    if(IS_COMPLETED(Reset_state_48) == false)
        {
            return false;
        }
    return true;
}

void Limetten::state_4_Reset_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Reset");
    pushNullTransition();
    state_4_subState = state_4_Reset;
    state_4_active = state_4_Reset;
    Reset_state_47_entDef();
    Reset_state_48_entDef();
}

void Limetten::state_4_Reset_exit() {
    popNullTransition();
    switch (Reset_state_47_subState) {
        // State SchneiderZuruck
        case state_47_SchneiderZuruck:
        {
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_47.SchneiderZuruck");
        }
        break;
        // State terminationstate_51
        case state_47_terminationstate_51:
        {
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_47.terminationstate_51");
        }
        break;
        default:
            break;
    }
    Reset_state_47_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_47");
    switch (Reset_state_48_subState) {
        // State SchieberZuruck
        case state_48_SchieberZuruck:
        {
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_48.SchieberZuruck");
        }
        break;
        // State terminationstate_52
        case state_48_terminationstate_52:
        {
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_48.terminationstate_52");
        }
        break;
        default:
            break;
    }
    Reset_state_48_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_48");
    
    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Reset");
}

IOxfReactive::TakeEventStatus Limetten::state_4_ResetTakeNull() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    //## transition 16 
    if(IS_COMPLETED(state_4_Reset)==true)
        {
            //## transition 17 
            if(TheLimette)
                {
                    NOTIFY_TRANSITION_STARTED("16");
                    NOTIFY_TRANSITION_STARTED("17");
                    state_4_Reset_exit();
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Stopped");
                    state_4_subState = Stopped;
                    state_4_active = Stopped;
                    //#[ state Betrieb.state_4.Stopped.(Entry) 
                    Error = true;
                    //#]
                    NOTIFY_TRANSITION_TERMINATED("17");
                    NOTIFY_TRANSITION_TERMINATED("16");
                    res = eventConsumed;
                }
            else
                {
                    NOTIFY_TRANSITION_STARTED("16");
                    NOTIFY_TRANSITION_STARTED("18");
                    state_4_Reset_exit();
                    Idle_entDef();
                    NOTIFY_TRANSITION_TERMINATED("18");
                    NOTIFY_TRANSITION_TERMINATED("16");
                    res = eventConsumed;
                }
        }
    return res;
}

IOxfReactive::TakeEventStatus Limetten::state_4_Reset_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    // State state_47
    if(Reset_state_47_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(state_4_Reset))
                {
                    return res;
                }
        }
    // State state_48
    if(Reset_state_48_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(state_4_Reset))
                {
                    return res;
                }
        }
    if(res == eventNotConsumed)
        {
            res = state_4_Reset_handleEvent();
        }
    return res;
}

IOxfReactive::TakeEventStatus Limetten::state_4_Reset_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(OMNullEventId))
        {
            res = state_4_ResetTakeNull();
        }
    
    
    return res;
}

void Limetten::Reset_state_48_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_48");
    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Reset.1");
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_48.SchieberZuruck");
    Reset_state_48_subState = state_48_SchieberZuruck;
    Reset_state_48_active = state_48_SchieberZuruck;
    //#[ state Betrieb.state_4.Reset.Reset.state_48.SchieberZuruck.(Entry) 
    itsSchieber.setDown(false);
      itsSchieber.GEN(evRun());
    //#]
    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Reset.1");
}

IOxfReactive::TakeEventStatus Limetten::Reset_state_48_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (Reset_state_48_active) {
        // State SchieberZuruck
        case state_48_SchieberZuruck:
        {
            if(IS_EVENT_TYPE_OF(evReady_System_id))
                {
                    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Reset.2");
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_48.SchieberZuruck");
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_48.terminationstate_52");
                    Reset_state_48_subState = state_48_terminationstate_52;
                    Reset_state_48_active = state_48_terminationstate_52;
                    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Reset.2");
                    res = eventConsumed;
                }
            
            
        }
        break;
        
        default:
            break;
    }
    return res;
}

void Limetten::Reset_state_47_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_47");
    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Reset.0");
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_47.SchneiderZuruck");
    Reset_state_47_subState = state_47_SchneiderZuruck;
    Reset_state_47_active = state_47_SchneiderZuruck;
    //#[ state Betrieb.state_4.Reset.Reset.state_47.SchneiderZuruck.(Entry) 
    itsSchneider.setDown(false); 
    itsSchneider.GEN(evRun()); 
    //#]
    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Reset.0");
}

IOxfReactive::TakeEventStatus Limetten::Reset_state_47_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (Reset_state_47_active) {
        // State SchneiderZuruck
        case state_47_SchneiderZuruck:
        {
            if(IS_EVENT_TYPE_OF(evSReady_System_id))
                {
                    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Reset.3");
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_47.SchneiderZuruck");
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_47.terminationstate_51");
                    Reset_state_47_subState = state_47_terminationstate_51;
                    Reset_state_47_active = state_47_terminationstate_51;
                    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Reset.3");
                    res = eventConsumed;
                }
            
            
        }
        break;
        
        default:
            break;
    }
    return res;
}

void Limetten::Idle_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Idle");
    state_4_subState = Idle;
    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Idle.1");
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Idle.ROOT.Idle.beide_up");
    pushNullTransition();
    Idle_subState = beide_up;
    state_4_active = beide_up;
    Idle_timeout = scheduleTimeout(1, "ROOT.Betrieb.state_4.Idle.ROOT.Idle.beide_up");
    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Idle.1");
}

IOxfReactive::TakeEventStatus Limetten::Idle_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(evRun_System_id))
        {
            //## transition 1 
            if(checkGlas())
                {
                    NOTIFY_TRANSITION_STARTED("1");
                    switch (Idle_subState) {
                        // State beide_up
                        case beide_up:
                        {
                            popNullTransition();
                            cancel(Idle_timeout);
                            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Idle.ROOT.Idle.beide_up");
                        }
                        break;
                        // State terminationstate_33
                        case terminationstate_33:
                        {
                            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Idle.ROOT.Idle.terminationstate_33");
                        }
                        break;
                        default:
                            break;
                    }
                    Idle_subState = OMNonState;
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Idle");
                    //#[ transition 1 
                    setTara();
                    //#]
                    Running_entDef();
                    NOTIFY_TRANSITION_TERMINATED("1");
                    res = eventConsumed;
                }
        }
    
    
    return res;
}

IOxfReactive::TakeEventStatus Limetten::beide_up_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(OMTimeoutEventId))
        {
            if(getCurrentEvent() == Idle_timeout)
                {
                    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Idle.0");
                    popNullTransition();
                    cancel(Idle_timeout);
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Idle.ROOT.Idle.beide_up");
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Idle.ROOT.Idle.beide_up");
                    pushNullTransition();
                    Idle_subState = beide_up;
                    state_4_active = beide_up;
                    Idle_timeout = scheduleTimeout(1, "ROOT.Betrieb.state_4.Idle.ROOT.Idle.beide_up");
                    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Idle.0");
                    res = eventConsumed;
                }
        }
    else if(IS_EVENT_TYPE_OF(OMNullEventId))
        {
            //## transition Betrieb.state_4.Idle.2 
            if(itsSchneider.getPosition() >= 100 && itsSchieber.getPosition() >= 100)
                {
                    NOTIFY_TRANSITION_STARTED("ROOT.Betrieb.state_4.Idle.2");
                    popNullTransition();
                    cancel(Idle_timeout);
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Idle.ROOT.Idle.beide_up");
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Idle.ROOT.Idle.terminationstate_33");
                    Idle_subState = terminationstate_33;
                    state_4_active = terminationstate_33;
                    NOTIFY_TRANSITION_TERMINATED("ROOT.Betrieb.state_4.Idle.2");
                    res = eventConsumed;
                }
        }
    
    if(res == eventNotConsumed)
        {
            res = Idle_handleEvent();
        }
    return res;
}

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedLimetten::serializeAttributes(AOMSAttributes* aomsAttributes) const {
    aomsAttributes->addAttribute("TheLimette", x2String(myReal->TheLimette));
    OMAnimatedAbfuellstation::serializeAttributes(aomsAttributes);
}

void OMAnimatedLimetten::serializeRelations(AOMSRelations* aomsRelations) const {
    aomsRelations->addRelation("itsSchneider", true, true);
    aomsRelations->ADD_ITEM(&myReal->itsSchneider);
    aomsRelations->addRelation("itsSchieber", true, true);
    aomsRelations->ADD_ITEM(&myReal->itsSchieber);
    aomsRelations->addRelation("itsLichtschranke", false, true);
    if(myReal->itsLichtschranke)
        {
            aomsRelations->ADD_ITEM(myReal->itsLichtschranke);
        }
    OMAnimatedAbfuellstation::serializeRelations(aomsRelations);
}

void OMAnimatedLimetten::rootState_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT");
    if(myReal->rootState_subState == Limetten::Betrieb)
        {
            Betrieb_serializeStates(aomsState);
        }
}

void OMAnimatedLimetten::Betrieb_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb");
    state_4_serializeStates(aomsState);
    state_5_serializeStates(aomsState);
}

void OMAnimatedLimetten::state_5_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_5");
    switch (myReal->state_5_subState) {
        case Limetten::Offen:
        {
            Offen_serializeStates(aomsState);
        }
        break;
        case Limetten::Zu:
        {
            Zu_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedLimetten::Zu_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_5.Zu");
}

void OMAnimatedLimetten::Offen_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_5.Offen");
}

void OMAnimatedLimetten::state_4_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4");
    switch (myReal->state_4_subState) {
        case Limetten::Idle:
        {
            Idle_serializeStates(aomsState);
        }
        break;
        case Limetten::Running:
        {
            Running_serializeStates(aomsState);
        }
        break;
        case Limetten::Stopped:
        {
            Stopped_serializeStates(aomsState);
        }
        break;
        case Limetten::state_4_Reset:
        {
            state_4_Reset_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedLimetten::Stopped_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Stopped");
}

void OMAnimatedLimetten::Running_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running");
    switch (myReal->Running_subState) {
        case Limetten::terminationstate_11:
        {
            terminationstate_11_serializeStates(aomsState);
        }
        break;
        case Limetten::Schieben:
        {
            Schieben_serializeStates(aomsState);
        }
        break;
        case Limetten::Check:
        {
            Check_serializeStates(aomsState);
        }
        break;
        case Limetten::Schneider:
        {
            Schneider_serializeStates(aomsState);
        }
        break;
        case Limetten::Reset:
        {
            Reset_serializeStates(aomsState);
        }
        break;
        case Limetten::Check_2:
        {
            Check_2_serializeStates(aomsState);
        }
        break;
        case Limetten::ContinueHelperState:
        {
            ContinueHelperState_serializeStates(aomsState);
        }
        break;
        case Limetten::Running_ContinueHelperState:
        {
            Running_ContinueHelperState_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedLimetten::terminationstate_11_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.terminationstate_11");
}

void OMAnimatedLimetten::Schneider_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.Schneider");
}

void OMAnimatedLimetten::Schieben_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.Schieben");
}

void OMAnimatedLimetten::Reset_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset");
    state_47_serializeStates(aomsState);
    state_48_serializeStates(aomsState);
}

void OMAnimatedLimetten::state_48_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_48");
    switch (myReal->state_48_subState) {
        case Limetten::SchieberZuruck:
        {
            SchieberZuruck_serializeStates(aomsState);
        }
        break;
        case Limetten::terminationstate_52:
        {
            terminationstate_52_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedLimetten::terminationstate_52_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_48.terminationstate_52");
}

void OMAnimatedLimetten::SchieberZuruck_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_48.SchieberZuruck");
}

void OMAnimatedLimetten::state_47_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_47");
    switch (myReal->state_47_subState) {
        case Limetten::SchneiderZuruck:
        {
            SchneiderZuruck_serializeStates(aomsState);
        }
        break;
        case Limetten::terminationstate_51:
        {
            terminationstate_51_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedLimetten::terminationstate_51_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_47.terminationstate_51");
}

void OMAnimatedLimetten::SchneiderZuruck_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.Reset.ROOT.Reset.state_47.SchneiderZuruck");
}

void OMAnimatedLimetten::Running_ContinueHelperState_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.ContinueHelperState");
}

void OMAnimatedLimetten::ContinueHelperState_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.ContinueHelperState");
}

void OMAnimatedLimetten::Check_2_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.Check_2");
}

void OMAnimatedLimetten::Check_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running.ROOT.Running.Check");
}

void OMAnimatedLimetten::state_4_Reset_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Reset");
    Reset_state_47_serializeStates(aomsState);
    Reset_state_48_serializeStates(aomsState);
}

void OMAnimatedLimetten::Reset_state_48_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_48");
    switch (myReal->Reset_state_48_subState) {
        case Limetten::state_48_SchieberZuruck:
        {
            state_48_SchieberZuruck_serializeStates(aomsState);
        }
        break;
        case Limetten::state_48_terminationstate_52:
        {
            state_48_terminationstate_52_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedLimetten::state_48_terminationstate_52_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_48.terminationstate_52");
}

void OMAnimatedLimetten::state_48_SchieberZuruck_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_48.SchieberZuruck");
}

void OMAnimatedLimetten::Reset_state_47_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_47");
    switch (myReal->Reset_state_47_subState) {
        case Limetten::state_47_SchneiderZuruck:
        {
            state_47_SchneiderZuruck_serializeStates(aomsState);
        }
        break;
        case Limetten::state_47_terminationstate_51:
        {
            state_47_terminationstate_51_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedLimetten::state_47_terminationstate_51_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_47.terminationstate_51");
}

void OMAnimatedLimetten::state_47_SchneiderZuruck_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Reset.ROOT.Reset.state_47.SchneiderZuruck");
}

void OMAnimatedLimetten::Idle_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Idle");
    switch (myReal->Idle_subState) {
        case Limetten::beide_up:
        {
            beide_up_serializeStates(aomsState);
        }
        break;
        case Limetten::terminationstate_33:
        {
            terminationstate_33_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedLimetten::terminationstate_33_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Idle.ROOT.Idle.terminationstate_33");
}

void OMAnimatedLimetten::beide_up_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Idle.ROOT.Idle.beide_up");
}
//#]

IMPLEMENT_REACTIVE_META_S_P(Limetten, System, false, Abfuellstation, OMAnimatedAbfuellstation, OMAnimatedLimetten)

OMINIT_SUPERCLASS(Abfuellstation, OMAnimatedAbfuellstation)

OMREGISTER_REACTIVE_CLASS
#endif // _OMINSTRUMENT

//#[ ignore
evLIMReady_Limetten_Event::evLIMReady_Limetten_Event() {
    setId(evLIMReady_Limetten_Event_id);
}
//#]

/*********************************************************************
	File Path	: Systemkomponente/Simulation/Limetten.cpp
*********************************************************************/
