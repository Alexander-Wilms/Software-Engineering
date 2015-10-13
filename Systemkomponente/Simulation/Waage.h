/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Waage
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Waage.h
*********************************************************************/

#ifndef Waage_H
#define Waage_H

//## auto_generated
#include <oxf/oxf.h>
//## auto_generated
#include <aom/aom.h>
//## auto_generated
#include "System.h"
//## package System

//## class Waage
class Waage {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedWaage;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    Waage();
    
    //## auto_generated
    ~Waage();
    
    ////    Operations    ////
    
    //## operation addBrutto(int)
    void addBrutto(int aGewicht);
    
    //## operation clearBrutto()
    void clearBrutto();
    
    //## operation getNetto()
    int getNetto();
    
    //## operation setTara()
    void setTara();
    
    ////    Additional operations    ////
    
    //## auto_generated
    int getBrutto() const;
    
    //## auto_generated
    void setBrutto(int p_Brutto);
    
    //## auto_generated
    int getTara() const;
    
    //## auto_generated
    void setTara(int p_Tara);
    
    ////    Attributes    ////

protected :

    int Brutto;		//## attribute Brutto
    
    int Tara;		//## attribute Tara
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedWaage : virtual public AOMInstance {
    DECLARE_META(Waage, OMAnimatedWaage)
    
    ////    Framework operations    ////
    
public :

    virtual void serializeAttributes(AOMSAttributes* aomsAttributes) const;
};
//#]
#endif // _OMINSTRUMENT

#endif
/*********************************************************************
	File Path	: Systemkomponente/Simulation/Waage.h
*********************************************************************/
