import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CharacterComponent } from './character/character.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import { CharacterSideBarComponent } from './character-side-bar/character-side-bar.component';

@NgModule({
  declarations: [
    AppComponent,
    CharacterComponent,
    TopBarComponent,
    CharacterSideBarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
