/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Zucker
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Zucker.h
*********************************************************************/

#ifndef Zucker_H
#define Zucker_H

//## auto_generated
#include <oxf/oxf.h>
//## auto_generated
#include <aom/aom.h>
//## auto_generated
#include "System.h"
//## class Zucker
#include "Abfuellstation.h"
//## auto_generated
class Karussell;

//## auto_generated
class Kolben;

//## auto_generated
class Waage;

//## package System

//## class Zucker
class Zucker : public Abfuellstation {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedZucker;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    Zucker(IOxfActive* theActiveContext = 0);
    
    //## auto_generated
    ~Zucker();
    
    ////    Additional operations    ////
    
    //## auto_generated
    virtual bool startBehavior();

protected :

    //## auto_generated
    void initStatechart();
    
    //## auto_generated
    void cancelTimeouts();
    
    //## auto_generated
    bool cancelTimeout(const IOxfTimeout* arg);
    
    ////    Framework operations    ////
    
    ////    Framework    ////

public :

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
    IOxfReactive::TakeEventStatus state_4_processEvent();
    
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
    IOxfReactive::TakeEventStatus Running_handleEvent();
    
    // terminationstate_9:
    //## statechart_method
    inline bool terminationstate_9_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus terminationstate_9_handleEvent();
    
    // dosieren:
    //## statechart_method
    inline bool dosieren_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus dosieren_handleEvent();

protected :

//#[ ignore
    enum Zucker_Enum {
        terminationstate_9 = 9,
        dosieren = 10
    };
    
    int Running_subState;
    
    IOxfTimeout* Running_timeout;
//#]
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedZucker : public OMAnimatedAbfuellstation {
    DECLARE_REACTIVE_META(Zucker, OMAnimatedZucker)
    
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
    void terminationstate_9_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void dosieren_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Idle_serializeStates(AOMSState* aomsState) const;
};
//#]
#endif // _OMINSTRUMENT

inline bool Zucker::Running_IN() const {
    return state_4_subState == Running;
}

inline bool Zucker::Running_isCompleted() {
    return ( IS_IN(terminationstate_9) );
}

inline bool Zucker::terminationstate_9_IN() const {
    return Running_subState == terminationstate_9;
}

inline bool Zucker::dosieren_IN() const {
    return Running_subState == dosieren;
}

#endif
/*********************************************************************
	File Path	: Systemkomponente/Simulation/Zucker.h
*********************************************************************/
