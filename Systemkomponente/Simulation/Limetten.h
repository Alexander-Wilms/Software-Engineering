/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Limetten
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Limetten.h
*********************************************************************/

#ifndef Limetten_H
#define Limetten_H

//## auto_generated
#include <oxf/oxf.h>
//## auto_generated
#include <aom/aom.h>
//## auto_generated
#include "System.h"
//## class Limetten
#include "Abfuellstation.h"
//## classInstance itsSchieber
#include "Kolben.h"
//## classInstance itsSchneider
#include "Limettenschneider.h"
//## auto_generated
class Karussell;

//## link itsLichtschranke
class Lichtschranke;

//## auto_generated
class Waage;

//#[ ignore
#define evLIMReady_Limetten_Event_id 31001
//#]

//## package System

//## class Limetten
class Limetten : public Abfuellstation {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedLimetten;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## operation Limetten()
    Limetten(IOxfActive* theActiveContext = 0);
    
    //## auto_generated
    ~Limetten();
    
    ////    Operations    ////
    
    //## operation noLimette()
    void noLimette();
    
    ////    Additional operations    ////
    
    //## auto_generated
    bool getTheLimette() const;
    
    //## auto_generated
    void setTheLimette(bool p_TheLimette);
    
    //## auto_generated
    Lichtschranke* getItsLichtschranke() const;
    
    //## auto_generated
    void setItsLichtschranke(Lichtschranke* p_Lichtschranke);
    
    //## auto_generated
    Kolben* getItsSchieber() const;
    
    //## auto_generated
    Limettenschneider* getItsSchneider() const;
    
    //## auto_generated
    virtual bool startBehavior();

protected :

    //## auto_generated
    void initStatechart();
    
    //## auto_generated
    void cleanUpRelations();
    
    //## auto_generated
    void cancelTimeouts();
    
    //## auto_generated
    bool cancelTimeout(const IOxfTimeout* arg);

public :

    //## TriggeredOperation evLIMReady()
    void evLIMReady();
    
    ////    Attributes    ////

protected :

    bool TheLimette;		//## attribute TheLimette
    
    ////    Relations and components    ////
    
    Lichtschranke* itsLichtschranke;		//## link itsLichtschranke
    
    Kolben itsSchieber;		//## classInstance itsSchieber
    
    Limettenschneider itsSchneider;		//## classInstance itsSchneider
    
    ////    Framework operations    ////

public :

    //## auto_generated
    void setActiveContext(IOxfActive* theActiveContext, bool activeInstance);
    
    //## auto_generated
    virtual void destroy();
    
    ////    Framework    ////
    
    //## statechart_method
    virtual void rootState_entDef();
    
    //## statechart_method
    virtual IOxfReactive::TakeEventStatus rootState_processEvent();
    
    //## statechart_method
    void Betrieb_entDef();
    
    //## statechart_method
    void Betrieb_exit();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Betrieb_processEvent();
    
    //## statechart_method
    void state_5_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_5_processEvent();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Offen_handleEvent();
    
    //## statechart_method
    void state_4_entDef();
    
    //## statechart_method
    void state_4_exit();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_4_processEvent();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus StoppedTakeevContinue();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Stopped_handleEvent();
    
    // Running:
    //## statechart_method
    inline bool Running_IN() const;
    
    //## statechart_method
    inline bool Running_isCompleted();
    
    //## statechart_method
    void Running_exit();
    
    //## statechart_method
    void Running_entDef();
    
    //## statechart_method
    void Running_entShallowHist();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Running_handleEvent();
    
    // terminationstate_11:
    //## statechart_method
    inline bool terminationstate_11_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus terminationstate_11_handleEvent();
    
    // Schneider:
    //## statechart_method
    inline bool Schneider_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Schneider_handleEvent();
    
    // Schieben:
    //## statechart_method
    inline bool Schieben_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Schieben_handleEvent();
    
    // Reset:
    //## statechart_method
    inline bool Reset_IN() const;
    
    //## statechart_method
    bool Reset_isCompleted();
    
    //## statechart_method
    void Reset_entDef();
    
    //## statechart_method
    void Reset_exit();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Reset_processEvent();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Reset_handleEvent();
    
    // state_48:
    //## statechart_method
    inline bool state_48_IN() const;
    
    //## statechart_method
    inline bool state_48_isCompleted();
    
    //## statechart_method
    void state_48_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_48_processEvent();
    
    // terminationstate_52:
    //## statechart_method
    inline bool terminationstate_52_IN() const;
    
    // SchieberZuruck:
    //## statechart_method
    inline bool SchieberZuruck_IN() const;
    
    // state_47:
    //## statechart_method
    inline bool state_47_IN() const;
    
    //## statechart_method
    inline bool state_47_isCompleted();
    
    //## statechart_method
    void state_47_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_47_processEvent();
    
    // terminationstate_51:
    //## statechart_method
    inline bool terminationstate_51_IN() const;
    
    // SchneiderZuruck:
    //## statechart_method
    inline bool SchneiderZuruck_IN() const;
    
    // Running_ContinueHelperState:
    //## statechart_method
    inline bool Running_ContinueHelperState_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Running_ContinueHelperState_handleEvent();
    
    // ContinueHelperState:
    //## statechart_method
    inline bool ContinueHelperState_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus ContinueHelperState_handleEvent();
    
    // Check_2:
    //## statechart_method
    inline bool Check_2_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Check_2_handleEvent();
    
    // Check:
    //## statechart_method
    inline bool Check_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Check_handleEvent();
    
    // state_4_Reset:
    //## statechart_method
    inline bool state_4_Reset_IN() const;
    
    //## statechart_method
    bool state_4_Reset_isCompleted();
    
    //## statechart_method
    void state_4_Reset_entDef();
    
    //## statechart_method
    void state_4_Reset_exit();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_4_ResetTakeNull();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_4_Reset_processEvent();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_4_Reset_handleEvent();
    
    // Reset_state_48:
    //## statechart_method
    inline bool Reset_state_48_IN() const;
    
    //## statechart_method
    inline bool Reset_state_48_isCompleted();
    
    //## statechart_method
    void Reset_state_48_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Reset_state_48_processEvent();
    
    // state_48_terminationstate_52:
    //## statechart_method
    inline bool state_48_terminationstate_52_IN() const;
    
    // state_48_SchieberZuruck:
    //## statechart_method
    inline bool state_48_SchieberZuruck_IN() const;
    
    // Reset_state_47:
    //## statechart_method
    inline bool Reset_state_47_IN() const;
    
    //## statechart_method
    inline bool Reset_state_47_isCompleted();
    
    //## statechart_method
    void Reset_state_47_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Reset_state_47_processEvent();
    
    // state_47_terminationstate_51:
    //## statechart_method
    inline bool state_47_terminationstate_51_IN() const;
    
    // state_47_SchneiderZuruck:
    //## statechart_method
    inline bool state_47_SchneiderZuruck_IN() const;
    
    // Idle:
    //## statechart_method
    inline bool Idle_IN() const;
    
    //## statechart_method
    inline bool Idle_isCompleted();
    
    //## statechart_method
    void Idle_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Idle_handleEvent();
    
    // terminationstate_33:
    //## statechart_method
    inline bool terminationstate_33_IN() const;
    
    // beide_up:
    //## statechart_method
    inline bool beide_up_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus beide_up_handleEvent();

protected :

//#[ ignore
    enum Limetten_Enum {
        terminationstate_11 = 9,
        Schneider = 10,
        Schieben = 11,
        Reset = 12,
        state_48 = 13,
        terminationstate_52 = 14,
        SchieberZuruck = 15,
        state_47 = 16,
        terminationstate_51 = 17,
        SchneiderZuruck = 18,
        Running_ContinueHelperState = 19,
        ContinueHelperState = 20,
        Check_2 = 21,
        Check = 22,
        state_4_Reset = 23,
        Reset_state_48 = 24,
        state_48_terminationstate_52 = 25,
        state_48_SchieberZuruck = 26,
        Reset_state_47 = 27,
        state_47_terminationstate_51 = 28,
        state_47_SchneiderZuruck = 29,
        terminationstate_33 = 30,
        beide_up = 31
    };
    
    int Running_subState;
    
    int Running_lastState;
    
    int state_48_subState;
    
    int state_48_active;
    
    int state_47_subState;
    
    int state_47_active;
    
    int Reset_state_48_subState;
    
    int Reset_state_48_active;
    
    int Reset_state_47_subState;
    
    int Reset_state_47_active;
    
    int Idle_subState;
    
    IOxfTimeout* Idle_timeout;
//#]
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedLimetten : public OMAnimatedAbfuellstation {
    DECLARE_REACTIVE_META(Limetten, OMAnimatedLimetten)
    
    ////    Framework operations    ////
    
public :

    virtual void serializeAttributes(AOMSAttributes* aomsAttributes) const;
    
    virtual void serializeRelations(AOMSRelations* aomsRelations) const;
    
    //## statechart_method
    void rootState_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Betrieb_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_5_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Zu_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Offen_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_4_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Stopped_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Running_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void terminationstate_11_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Schneider_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Schieben_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Reset_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_48_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void terminationstate_52_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void SchieberZuruck_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_47_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void terminationstate_51_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void SchneiderZuruck_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Running_ContinueHelperState_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void ContinueHelperState_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Check_2_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Check_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_4_Reset_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Reset_state_48_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_48_terminationstate_52_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_48_SchieberZuruck_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Reset_state_47_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_47_terminationstate_51_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_47_SchneiderZuruck_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Idle_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void terminationstate_33_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void beide_up_serializeStates(AOMSState* aomsState) const;
};
//#]
#endif // _OMINSTRUMENT

//#[ ignore
class evLIMReady_Limetten_Event : public OMEvent {
    ////    Constructors and destructors    ////
    
public :

    evLIMReady_Limetten_Event();
};
//#]

inline bool Limetten::Running_IN() const {
    return state_4_subState == Running;
}

inline bool Limetten::Running_isCompleted() {
    return ( IS_IN(terminationstate_11) );
}

inline bool Limetten::terminationstate_11_IN() const {
    return Running_subState == terminationstate_11;
}

inline bool Limetten::Schneider_IN() const {
    return Running_subState == Schneider;
}

inline bool Limetten::Schieben_IN() const {
    return Running_subState == Schieben;
}

inline bool Limetten::Reset_IN() const {
    return Running_subState == Reset;
}

inline bool Limetten::state_48_IN() const {
    return Reset_IN();
}

inline bool Limetten::state_48_isCompleted() {
    return ( IS_IN(terminationstate_52) );
}

inline bool Limetten::terminationstate_52_IN() const {
    return state_48_subState == terminationstate_52;
}

inline bool Limetten::SchieberZuruck_IN() const {
    return state_48_subState == SchieberZuruck;
}

inline bool Limetten::state_47_IN() const {
    return Reset_IN();
}

inline bool Limetten::state_47_isCompleted() {
    return ( IS_IN(terminationstate_51) );
}

inline bool Limetten::terminationstate_51_IN() const {
    return state_47_subState == terminationstate_51;
}

inline bool Limetten::SchneiderZuruck_IN() const {
    return state_47_subState == SchneiderZuruck;
}

inline bool Limetten::Running_ContinueHelperState_IN() const {
    return Running_subState == Running_ContinueHelperState;
}

inline bool Limetten::ContinueHelperState_IN() const {
    return Running_subState == ContinueHelperState;
}

inline bool Limetten::Check_2_IN() const {
    return Running_subState == Check_2;
}

inline bool Limetten::Check_IN() const {
    return Running_subState == Check;
}

inline bool Limetten::state_4_Reset_IN() const {
    return state_4_subState == state_4_Reset;
}

inline bool Limetten::Reset_state_48_IN() const {
    return state_4_Reset_IN();
}

inline bool Limetten::Reset_state_48_isCompleted() {
    return ( IS_IN(state_48_terminationstate_52) );
}

inline bool Limetten::state_48_terminationstate_52_IN() const {
    return Reset_state_48_subState == state_48_terminationstate_52;
}

inline bool Limetten::state_48_SchieberZuruck_IN() const {
    return Reset_state_48_subState == state_48_SchieberZuruck;
}

inline bool Limetten::Reset_state_47_IN() const {
    return state_4_Reset_IN();
}

inline bool Limetten::Reset_state_47_isCompleted() {
    return ( IS_IN(state_47_terminationstate_51) );
}

inline bool Limetten::state_47_terminationstate_51_IN() const {
    return Reset_state_47_subState == state_47_terminationstate_51;
}

inline bool Limetten::state_47_SchneiderZuruck_IN() const {
    return Reset_state_47_subState == state_47_SchneiderZuruck;
}

inline bool Limetten::Idle_IN() const {
    return state_4_subState == Idle;
}

inline bool Limetten::Idle_isCompleted() {
    return ( IS_IN(terminationstate_33) );
}

inline bool Limetten::terminationstate_33_IN() const {
    return Idle_subState == terminationstate_33;
}

inline bool Limetten::beide_up_IN() const {
    return Idle_subState == beide_up;
}

#endif
/*********************************************************************
	File Path	: Systemkomponente/Simulation/Limetten.h
*********************************************************************/
