/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Vorrat
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Vorrat.h
*********************************************************************/

#ifndef Vorrat_H
#define Vorrat_H

//## auto_generated
#include <oxf/oxf.h>
//## auto_generated
#include <aom/aom.h>
//## auto_generated
#include "System.h"
//## package System

//## class Vorrat
class Vorrat {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedVorrat;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    Vorrat();
    
    //## auto_generated
    ~Vorrat();
    
    ////    Operations    ////
    
    //## operation entnehme(int)
    int entnehme(int aMenge);
    
    //## operation fuelle()
    void fuelle();
    
    //## operation getVorrat()
    int getVorrat();
    
    //## operation setMaxVorrat(int)
    void setMaxVorrat(int input);
    
    //## operation setVorhandenerVorrat(int)
    void setVorhandenerVorrat(int input);
    
    ////    Additional operations    ////
    
    //## auto_generated
    int getMaxVorrat() const;
    
    //## auto_generated
    int getVorhandenerVorrat() const;
    
    ////    Attributes    ////

protected :

    int MaxVorrat;		//## attribute MaxVorrat
    
    int VorhandenerVorrat;		//## attribute VorhandenerVorrat
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedVorrat : virtual public AOMInstance {
    DECLARE_META(Vorrat, OMAnimatedVorrat)
    
    ////    Framework operations    ////
    
public :

    virtual void serializeAttributes(AOMSAttributes* aomsAttributes) const;
};
//#]
#endif // _OMINSTRUMENT

#endif
/*********************************************************************
	File Path	: Systemkomponente/Simulation/Vorrat.h
*********************************************************************/
