/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Kolben
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Kolben.h
*********************************************************************/

#ifndef Kolben_H
#define Kolben_H

//## auto_generated
#include <oxf/oxf.h>
//## auto_generated
#include <aom/aom.h>
//## auto_generated
#include "System.h"
//## auto_generated
#include <oxf/omthread.h>
//## auto_generated
#include <oxf/omreactive.h>
//## auto_generated
#include <oxf/state.h>
//## auto_generated
#include <oxf/event.h>
//## link itsStation
class Station;

//## package System

//## class Kolben
class Kolben : public OMReactive {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedKolben;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    Kolben(IOxfActive* theActiveContext = 0);
    
    //## auto_generated
    ~Kolben();
    
    ////    Operations    ////
    
    //## operation getPosition()
    int getPosition();
    
    //## operation run()
    void run();
    
    //## operation setDown(bool)
    void setDown(bool direction);
    
    ////    Additional operations    ////
    
    //## auto_generated
    bool getDown() const;
    
    //## auto_generated
    int getMaxPos() const;
    
    //## auto_generated
    void setMaxPos(int p_MaxPos);
    
    //## auto_generated
    int getPos() const;
    
    //## auto_generated
    void setPos(int p_Pos);
    
    //## auto_generated
    Station* getItsStation() const;
    
    //## auto_generated
    void setItsStation(Station* p_Station);
    
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
    
    ////    Attributes    ////
    
    bool Down;		//## attribute Down
    
    int MaxPos;		//## attribute MaxPos
    
    int Pos;		//## attribute Pos
    
    ////    Relations and components    ////
    
    Station* itsStation;		//## link itsStation
    
    ////    Framework operations    ////

public :

    //## auto_generated
    void __setItsStation(Station* p_Station);
    
    //## auto_generated
    void _setItsStation(Station* p_Station);
    
    //## auto_generated
    void _clearItsStation();
    
    ////    Framework    ////
    
    // rootState:
    //## statechart_method
    inline bool rootState_IN() const;
    
    //## statechart_method
    virtual void rootState_entDef();
    
    //## statechart_method
    virtual IOxfReactive::TakeEventStatus rootState_processEvent();
    
    // Running:
    //## statechart_method
    inline bool Running_IN() const;
    
    // Idle:
    //## statechart_method
    inline bool Idle_IN() const;

protected :

//#[ ignore
    enum Kolben_Enum {
        OMNonState = 0,
        Running = 1,
        Idle = 2
    };
    
    int rootState_subState;
    
    int rootState_active;
    
    IOxfTimeout* rootState_timeout;
//#]
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedKolben : virtual public AOMInstance {
    DECLARE_REACTIVE_META(Kolben, OMAnimatedKolben)
    
    ////    Framework operations    ////
    
public :

    virtual void serializeAttributes(AOMSAttributes* aomsAttributes) const;
    
    virtual void serializeRelations(AOMSRelations* aomsRelations) const;
    
    //## statechart_method
    void rootState_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Running_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Idle_serializeStates(AOMSState* aomsState) const;
};
//#]
#endif // _OMINSTRUMENT

inline bool Kolben::rootState_IN() const {
    return true;
}

inline bool Kolben::Running_IN() const {
    return rootState_subState == Running;
}

inline bool Kolben::Idle_IN() const {
    return rootState_subState == Idle;
}

#endif
/*********************************************************************
	File Path	: Systemkomponente/Simulation/Kolben.h
*********************************************************************/
