/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Stampfer
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Stampfer.h
*********************************************************************/

#ifndef Stampfer_H
#define Stampfer_H

//## auto_generated
#include <oxf/oxf.h>
//## auto_generated
#include <aom/aom.h>
//## auto_generated
#include "System.h"
//## classInstance itsStampferkolben
#include "Kolben.h"
//## class Stampfer
#include "Station.h"
//## auto_generated
class Karussell;

//## auto_generated
class Waage;

//## package System

//## class Stampfer
class Stampfer : public Station {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedStampfer;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## operation Stampfer()
    Stampfer(IOxfActive* theActiveContext = 0);
    
    //## auto_generated
    ~Stampfer();
    
    ////    Additional operations    ////
    
    //## auto_generated
    int getRunde() const;
    
    //## auto_generated
    void setRunde(int p_runde);
    
    //## auto_generated
    Kolben* getItsStampferkolben() const;
    
    //## auto_generated
    virtual bool startBehavior();

protected :

    //## auto_generated
    void initStatechart();
    
    ////    Attributes    ////
    
    int runde;		//## attribute runde
    
    ////    Relations and components    ////
    
    Kolben itsStampferkolben;		//## classInstance itsStampferkolben
    
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
    
    // Up:
    //## statechart_method
    inline bool Up_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Up_handleEvent();
    
    // terminationstate_22:
    //## statechart_method
    inline bool terminationstate_22_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus terminationstate_22_handleEvent();
    
    // Down:
    //## statechart_method
    inline bool Down_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Down_handleEvent();

protected :

//#[ ignore
    enum Stampfer_Enum {
        Up = 9,
        terminationstate_22 = 10,
        Down = 11
    };
    
    int Running_subState;
//#]
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedStampfer : public OMAnimatedStation {
    DECLARE_REACTIVE_META(Stampfer, OMAnimatedStampfer)
    
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
    void Up_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void terminationstate_22_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Down_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Idle_serializeStates(AOMSState* aomsState) const;
};
//#]
#endif // _OMINSTRUMENT

inline bool Stampfer::Running_IN() const {
    return state_4_subState == Running;
}

inline bool Stampfer::Running_isCompleted() {
    return ( IS_IN(terminationstate_22) );
}

inline bool Stampfer::Up_IN() const {
    return Running_subState == Up;
}

inline bool Stampfer::terminationstate_22_IN() const {
    return Running_subState == terminationstate_22;
}

inline bool Stampfer::Down_IN() const {
    return Running_subState == Down;
}

#endif
/*********************************************************************
	File Path	: Systemkomponente/Simulation/Stampfer.h
*********************************************************************/
