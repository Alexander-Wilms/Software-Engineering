/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Simulation
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/MainSystemkomponente.cpp
*********************************************************************/

//## auto_generated
#include "MainSystemkomponente.h"
//## auto_generated
#include "System.h"
Systemkomponente::Systemkomponente() {
    System_initRelations();
    System_startBehavior();
}

int main(int argc, char* argv[]) {
    int status = 0;
    if(OXF::initialize(argc, argv, 6423))
        {
            Systemkomponente initializer_Systemkomponente;
            //#[ configuration Systemkomponente::Simulation 
            //#]
            OXF::start();
            status = 0;
        }
    else
        {
            status = 1;
        }
    return status;
}

/*********************************************************************
	File Path	: Systemkomponente/Simulation/MainSystemkomponente.cpp
*********************************************************************/
