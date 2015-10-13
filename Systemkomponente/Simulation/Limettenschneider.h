/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Limettenschneider
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Limettenschneider.h
*********************************************************************/

#ifndef Limettenschneider_H
#define Limettenschneider_H

//## auto_generated
#include <oxf/oxf.h>
//## auto_generated
#include <aom/aom.h>
//## auto_generated
#include "System.h"
//## class Limettenschneider
#include "Kolben.h"
//## auto_generated
class Station;

//## package System

//## class Limettenschneider
class Limettenschneider : public Kolben {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedLimettenschneider;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    Limettenschneider(IOxfActive* theActiveContext = 0);
    
    //## auto_generated
    ~Limettenschneider();
    
    ////    Operations    ////
    
    //## operation run()
    void run();
    
    ////    Additional operations    ////
    
    //## auto_generated
    virtual bool startBehavior();

protected :

    //## auto_generated
    void initStatechart();
    
    ////    Framework operations    ////

public :

    //## statechart_method
    virtual void rootState_entDef();
    
    //## statechart_method
    virtual IOxfReactive::TakeEventStatus rootState_processEvent();
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedLimettenschneider : public OMAnimatedKolben {
    DECLARE_REACTIVE_META(Limettenschneider, OMAnimatedLimettenschneider)
    
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

#endif
/*********************************************************************
	File Path	: Systemkomponente/Simulation/Limettenschneider.h
*********************************************************************/
