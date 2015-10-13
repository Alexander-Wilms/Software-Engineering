/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Tuer
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Tuer.h
*********************************************************************/

#ifndef Tuer_H
#define Tuer_H

//## auto_generated
#include <oxf/oxf.h>
//## auto_generated
#include <aom/aom.h>
//## auto_generated
#include "System.h"
//#[ ignore
#define OMAnim_System_Tuer_setZustand_bool_ARGS_DECLARATION bool p_Zustand;
//#]

//## package System

//## class Tuer
class Tuer {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedTuer;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    Tuer();
    
    //## auto_generated
    ~Tuer();
    
    ////    Operations    ////
    
    //## operation getZustand()
    bool getZustand();
    
    //## operation open()
    void open();
    
    ////    Additional operations    ////
    
    //## auto_generated
    void setZustand(bool p_Zustand);
    
    ////    Attributes    ////

protected :

    bool Zustand;		//## attribute Zustand
};

#ifdef _OMINSTRUMENT
DECLARE_OPERATION_CLASS(System_Tuer_setZustand_bool)

//#[ ignore
class OMAnimatedTuer : virtual public AOMInstance {
    DECLARE_META(Tuer, OMAnimatedTuer)
    
    DECLARE_META_OP(System_Tuer_setZustand_bool)
    
    ////    Framework operations    ////
    
public :

    virtual void serializeAttributes(AOMSAttributes* aomsAttributes) const;
};
//#]
#endif // _OMINSTRUMENT

#endif
/*********************************************************************
	File Path	: Systemkomponente/Simulation/Tuer.h
*********************************************************************/
