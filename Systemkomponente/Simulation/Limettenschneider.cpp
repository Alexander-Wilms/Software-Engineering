/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Limettenschneider
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Limettenschneider.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX

#define _OMSTATECHART_ANIMATED
//#]

//## auto_generated
#include "Limettenschneider.h"
//## auto_generated
#include "Station.h"
//#[ ignore
#define System_Limettenschneider_Limettenschneider_SERIALIZE OM_NO_OP

#define System_Limettenschneider_run_SERIALIZE OM_NO_OP
//#]

//## package System

//## class Limettenschneider
Limettenschneider::Limettenschneider(IOxfActive* theActiveContext) {
    NOTIFY_REACTIVE_CONSTRUCTOR(Limettenschneider, Limettenschneider(), 0, System_Limettenschneider_Limettenschneider_SERIALIZE);
    setActiveContext(theActiveContext, false);
    initStatechart();
}

Limettenschneider::~Limettenschneider() {
    NOTIFY_DESTRUCTOR(~Limettenschneider, false);
}

void Limettenschneider::run() {
    NOTIFY_OPERATION(run, run(), 0, System_Limettenschneider_run_SERIALIZE);
    //#[ operation run()
    if(!Down && Pos < MaxPos)	Pos +=10;
    else if(Down && Pos > 0)	Pos -= 10;
    else if(!Down && Pos >= MaxPos) {   
    	itsStation->GEN(evSReady);    
    }            
    else if(Down && Pos <= 0) {    
    
    	itsStation->GEN(evSReady);
    } 
           
    
    //#]
}

bool Limettenschneider::startBehavior() {
    bool done = false;
    done = Kolben::startBehavior();
    return done;
}

void Limettenschneider::initStatechart() {
    rootState_subState = OMNonState;
    rootState_active = OMNonState;
}

void Limettenschneider::rootState_entDef() {
    {
        NOTIFY_STATE_ENTERED("ROOT");
        NOTIFY_TRANSITION_STARTED("0");
        NOTIFY_STATE_ENTERED("ROOT.Idle");
        rootState_subState = Idle;
        rootState_active = Idle;
        NOTIFY_TRANSITION_TERMINATED("0");
    }
}

IOxfReactive::TakeEventStatus Limettenschneider::rootState_processEvent() {
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
void OMAnimatedLimettenschneider::serializeAttributes(AOMSAttributes* aomsAttributes) const {
    OMAnimatedKolben::serializeAttributes(aomsAttributes);
}

void OMAnimatedLimettenschneider::serializeRelations(AOMSRelations* aomsRelations) const {
    OMAnimatedKolben::serializeRelations(aomsRelations);
}

void OMAnimatedLimettenschneider::rootState_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT");
    switch (myReal->rootState_subState) {
        case Limettenschneider::Idle:
        {
            Idle_serializeStates(aomsState);
        }
        break;
        case Limettenschneider::Running:
        {
            Running_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedLimettenschneider::Running_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Running");
}

void OMAnimatedLimettenschneider::Idle_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Idle");
}
//#]

IMPLEMENT_REACTIVE_META_S_P(Limettenschneider, System, false, Kolben, OMAnimatedKolben, OMAnimatedLimettenschneider)

OMINIT_SUPERCLASS(Kolben, OMAnimatedKolben)

OMREGISTER_REACTIVE_CLASS
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: Systemkomponente/Simulation/Limettenschneider.cpp
*********************************************************************/
