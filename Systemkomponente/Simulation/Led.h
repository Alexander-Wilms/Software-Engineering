/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Led
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Led.h
*********************************************************************/

#ifndef Led_H
#define Led_H

//## auto_generated
#include <oxf/oxf.h>
//## auto_generated
#include <aom/aom.h>
//## auto_generated
#include "System.h"
//## package System

//## class Led
class Led {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedLed;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    Led();
    
    //## auto_generated
    ~Led();
    
    ////    Additional operations    ////
    
    //## auto_generated
    bool getOn() const;
    
    //## auto_generated
    void setOn(bool p_On);
    
    ////    Attributes    ////

protected :

    bool On;		//## attribute On
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedLed : virtual public AOMInstance {
    DECLARE_META(Led, OMAnimatedLed)
    
    ////    Framework operations    ////
    
public :

    virtual void serializeAttributes(AOMSAttributes* aomsAttributes) const;
};
//#]
#endif // _OMINSTRUMENT

#endif
/*********************************************************************
	File Path	: Systemkomponente/Simulation/Led.h
*********************************************************************/
